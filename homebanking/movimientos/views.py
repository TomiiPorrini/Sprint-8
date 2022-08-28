from django.shortcuts import render
from .models import Movimientos

# Create your views here.

def movimientos(request):
    movimientos = Movimientos.objects.using('ITBANK').all()
    return render(request, 'movimientos/movimientos.html', {'movimientos': movimientos})