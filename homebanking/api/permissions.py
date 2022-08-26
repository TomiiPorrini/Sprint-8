from rest_framework import permissions
from .models import Cliente
from .models import Empleado

class esEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        nombre = request.user.first_name
        apellido = request.user.last_name
        
        if Empleado.objects.using('ITBANK').filter(employee_name=nombre, employee_surname=apellido):
            return True
        else:
            return False

class esEmpleadoOCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        nombre = request.user.first_name
        apellido = request.user.last_name

        
        if Empleado.objects.using('ITBANK').filter(employee_name=nombre, employee_surname=apellido):
            return True
        elif Cliente.objects.using('ITBANK').filter(customer_name=nombre, customer_surname=apellido):
            return True
        else:
            return False
