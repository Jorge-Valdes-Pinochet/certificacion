from django import forms
from .models import Bus, BusEstacionado

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['patente', 'empresa', 'estacionado']

class BusEstacionadoForm(forms.ModelForm):
    class Meta:
        model = BusEstacionado
        fields = ['llegada']