# gestion_imei/forms.py
from django import forms
from .models import Cell

class CellForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = ['marca', 'modelo', 'imei']

class CellEditForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = ['marca', 'modelo', 'imei', 'vendido', 'comprador', 'robado']
