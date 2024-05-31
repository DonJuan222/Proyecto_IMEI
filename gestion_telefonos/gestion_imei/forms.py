# gestion_imei/forms.py
from django import forms
from .models import Cell
from django.contrib.auth.models import User

class CellForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = ['marca', 'modelo', 'imei']

class CellEditForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = ['marca', 'modelo', 'imei', 'vendido', 'comprador', 'robado']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")