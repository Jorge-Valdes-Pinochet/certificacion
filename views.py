from datetime import timezone
from django.shortcuts import render
from .models import Terminal, Anden, Empresa, Bus, BusEstacionado

def home(request):
    return render(request, 'gestion/home.html')

def lista_terminales(request):
    terminales = Terminal.objects.all()
    return render(request, 'gestion/terminales.html', {'terminales': terminales})

def lista_andenes(request):
    andenes = Anden.objects.all()
    return render(request, 'gestion/andenes.html', {'andenes': andenes})

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'gestion/empresas.html', {'empresas': empresas})

def lista_buses(request):
    buses = Bus.objects.all()
    return render(request, 'gestion/buses.html', {'buses': buses})

def reporte_diario(request):
    buses_estacionados = BusEstacionado.objects.filter(llegada__date=timezone.now().date())
    return render(request, 'gestion/reporte_diario.html', {'buses_estacionados': buses_estacionados})