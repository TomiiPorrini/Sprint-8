from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
#importando serializadores.
from .serializers import ClienteSerializer
from .serializers import TarjetaSerializer
from .serializers import DireccionSerializer
from .serializers import CuentaSerializer
from .serializers import TipoCuentaSerializer
from .serializers import PrestamoSerializer
from .serializers import SucursalSerializer
#importando modelos.
from .models import Cliente, Sucursal
from .models import Tarjeta
from .models import Direccion
from .models import Cuenta
from .models import TipoCuenta
from .models import Prestamo

#importando permisos.
from rest_framework import permissions
from .permissions import esEmpleado
from .permissions import esCliente
from .permissions import esEmpleadoOCliente
# Create your views here.

class GetSucursales(APIView):
    
    def get(self, request):
        items = Sucursal.objects.using("ITBANK").all()
        serializer = SucursalSerializer(items, many=True)
        return Response(serializer.data)
        
        

class InfoCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, esCliente]

    def get(self, request, customer_DNI):
        nombre = request.user.first_name
        apellido = request.user.last_name

        cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).first()
        
        if cliente_buscado:
            if cliente_buscado.customer_name == nombre and cliente_buscado.customer_surname == apellido:
                serializer = ClienteSerializer(cliente_buscado)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No sos dueño de la info.", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("no existe un cliente con ese DNI.", status=status.HTTP_404_NOT_FOUND)


class SaldoYCuentaCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, esCliente]

    def get(self, request, customer_DNI):
        nombre = request.user.first_name
        apellido = request.user.last_name

        cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).first()
        
        if cliente_buscado:
            if cliente_buscado.customer_name == nombre and cliente_buscado.customer_surname == apellido:
                clienteId = cliente_buscado.customer_id
                cuentas = Cuenta.objects.using('ITBANK').filter(customer_id = clienteId).all()
                if cuentas:
                    
                    CuentasLista = []
                    for cuenta in cuentas:
                        tipoID = cuenta.type_account_id
                        tipoCuenta = TipoCuenta.objects.using('ITBANK').filter(account_type_id = tipoID).first()
                        diccionario = {"balance":cuenta.balance, "Tipo de Cuenta":tipoCuenta.account_type_description}
                        CuentasLista.append(diccionario)
                    
                    return Response(CuentasLista, status=status.HTTP_200_OK)
                else:
                    return Response("no existen cuentas asociadas al DNI.", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("No sos dueño de la info.", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("no existe un cliente con ese DNI.", status=status.HTTP_404_NOT_FOUND)


class MontoPrestamosCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, esCliente]

    def get(self, request, customer_DNI):
        nombre = request.user.first_name
        apellido = request.user.last_name

        cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).first()
        
        if cliente_buscado:
            if cliente_buscado.customer_name == nombre and cliente_buscado.customer_surname == apellido:
                clienteId = cliente_buscado.customer_id
                prestamos = Prestamo.objects.using('ITBANK').filter(customer_id = clienteId).all()
                if prestamos:
                    PrestamosLista = PrestamoSerializer(prestamos, many=True)
                    for prestamito in PrestamosLista.data:
                        del prestamito['loan_id']
                        del prestamito['loan_date']
                        del prestamito['customer_id']
                    return Response(PrestamosLista.data, status=status.HTTP_200_OK)
                else:
                    return Response("no existen cuentas asociadas al DNI.", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("No sos dueño de la info.", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("no existe un cliente con ese DNI.", status=status.HTTP_404_NOT_FOUND)


class TarjetasCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]

    def get(self, request, customer_DNI):
        cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).values().first()
        if cliente_buscado:
            customer_id = cliente_buscado['customer_id']
            tarjetas = Tarjeta.objects.using('ITBANK').filter(customer_id=customer_id)
            if tarjetas:
                serializer = TarjetaSerializer(tarjetas,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("no tiene tarjetas asociadas", status=status.HTTP_200_OK)
        else:
            return Response("no existe un cliente con ese DNI", status=status.HTTP_404_NOT_FOUND)


class DireccionCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleadoOCliente]
    
    def put(self, request, customer_DNI):
        Cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).values().first()
        if Cliente_buscado:
            if Cliente_buscado['customer_name'] == request.user.first_name and Cliente_buscado['customer_surname'] == request.user.last_name:
                customer_direccion_id = Cliente_buscado['customer_direccion_id']
                direccion = Direccion.objects.using('ITBANK').filter(direccion_id = customer_direccion_id).first()
                serializer = DireccionSerializer(direccion, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("No tiene acceso a esta info por ser un cliente distinto al de la informacion", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("no existe un cliente con ese DNI", status=status.HTTP_404_NOT_FOUND)



class AnularPrestamo(APIView):
    def delete(self, request, customer_DNI):
        
        # Getting cliente
        cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).values().first()
        if not cliente_buscado: raise "El cliente no existe"
        customer_id = cliente_buscado['customer_id']
        
        # Getting prestamo
        prestamo = Prestamo.objects.using('ITBANK').filter(customer_id=customer_id)
        if not prestamo: raise "El cliente no cuenta con prestamos"
        prestamo.delete()
        # Serializing
        serializer = AnularPrestamo(prestamo)
        if not serializer.is_valid(): raise "Hubo un problema con los serializadores"
        serializer.save()
        return response(serializer.data)


