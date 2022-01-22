from .models import Barber
from django import forms

class BarberForm(forms.ModelForm): 

    class Meta:
        model = Barber
        fields = [
            'name',
            'surname'           
        ]