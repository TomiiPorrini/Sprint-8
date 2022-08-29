
from datetime import date
from time import strftime
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
from .models import Sucursal

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

class PrestamosSucursal(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]

    def get(self, request, branch_id):
        sucursal_buscada = Sucursal.objects.using('ITBANK').filter(branch_id = branch_id).values().first()
        if sucursal_buscada:
            clientes = Cliente.objects.using('ITBANK').filter(branch_id=branch_id)
            ids = []
            for cliente in clientes:
                ids.append(cliente.customer_id)

            prestamos = []
            for id in ids:
                prestamos.extend(Prestamo.objects.using('ITBANK').filter(customer_id=id))

            if prestamos:
                serializer = PrestamoSerializer(prestamos,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("La Sucursal no tiene prestamos asociados", status=status.HTTP_200_OK)
                
        else:
            return Response("No existe una sucursal con ese nombre", status=status.HTTP_404_NOT_FOUND)

class SolicitudPrestamo(APIView):
    def post(self, request):
        data = request.data
        data['loan_date'] = date.today().strftime('%Y-%m-%d')
        serializer = PrestamoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("El prestamo ha sido enviado con exito", status=status.HTTP_201_CREATED) 
        return Response("No se pudo enviar el prestamo", status=status.HTTP_400_BAD_REQUEST)

class AnularPrestamo(APIView):
    def delete(self, request, customer_DNI):
        # Getting cliente
        cliente_buscado = Cliente.objects.using('ITBANK').filter(customer_dni = customer_DNI).values().first()
        if not cliente_buscado: raise "El cliente no existe"
        customer_id = cliente_buscado['customer_id']
        # Getting prestamo
        prestamo = Prestamo.objects.using('ITBANK').filter(customer_id=customer_id)
        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            prestamo.delete()
            return Response("El prestamo se ha eliminado con exito", status=status.HTTP_201_CREATED)
        return Response("Hubo un error en la solicitud", status=status.HTTP_400_BAD_REQUEST)
        
        """ if not prestamo: raise "El cliente no cuenta con prestamos"
        # Serializing
        serializer = PrestamoSerializer(prestamo)
        if not serializer.is_valid(): return Response("Hubo un error en la solicitud", status=status.HTTP_400_BAD_REQUEST)
        prestamo.delete()
        return Response("El prestamo se ha eliminado con exito", status=status.HTTP_201_CREATED) """


