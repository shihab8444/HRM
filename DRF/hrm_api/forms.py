from django import forms
from .models import employee

class MyForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['name', 'email', 'age', 'position', 'password1', 'password2']
