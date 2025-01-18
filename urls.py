from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('terminales/', views.lista_terminales, name='lista_terminales'),
    path('andenes/', views.lista_andenes, name='lista_andenes'),
    path('empresas/', views.lista_empresas, name='lista_empresas'),
    path('buses/', views.lista_buses, name='lista_buses'),
    path('reporte-diario/', views.reporte_diario, name='reporte_diario'),
]