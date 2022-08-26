from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

#importando serializadores.
from .serializers import ClienteSerializer
from .serializers import TarjetaSerializer
from .serializers import DireccionSerializer

#importando modelos.
from .models import Cliente
from .models import Tarjeta
from .models import Direccion

#importando permisos.
from rest_framework import permissions
from .permissions import esEmpleado
from .permissions import esEmpleadoOCliente

# Create your views here.
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


#agregar permiso, para que solo los empleados puedan acceder a esto.