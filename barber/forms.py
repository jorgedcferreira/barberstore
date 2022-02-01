from .models import Barber
from django import forms

class BarberForm(forms.ModelForm): 

    class Meta:
        model = Barber
        fields = [
            'name',
            'surname'           
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
        }