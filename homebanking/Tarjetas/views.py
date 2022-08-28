from django.shortcuts import render

# Create your views here.

def tarjetas(request):
    return render(request, "Tarjetas/tarjetas.html")

