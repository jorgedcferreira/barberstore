from cProfile import label
from dataclasses import field
import email
from logging import PlaceHolder
from turtle import title
from xml.dom import ValidationErr
from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    
    nif = forms.IntegerField(label = 'NIF', required=False)
    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'email',
            'date_of_birth',
            'nif',
            'preferred_barber',
            'preferred_store'
        ]
    

    #Validation on the form for the NIF
    def clean_nif(self, *args, **kwargs):
        """Checks if the NIF respects the portugues logic for personal fiscal number, with check digit. 
        See here: https://pt.wikipedia.org/wiki/N%C3%BAmero_de_identifica%C3%A7%C3%A3o_fiscal#Exemplo_de_valida%C3%A7%C3%A3o_em_Python"""

        EXPECTED_DIGITS = 9
        
        #converting nift to string but accepting empty nifs 
        if self.cleaned_data.get('nif'):
            nif = str(self.cleaned_data.get('nif'))
        else: 
            return None
        
        #Validation if nif has 9 digits
        if len(str(nif)) != EXPECTED_DIGITS: 
            raise forms.ValidationError(message= "NIF must have 9 digits lenght")

        #Validation of check digit
        sum_of_digits = sum([int(dig) * (EXPECTED_DIGITS - pos) for pos, dig in enumerate(nif)])
        rest = (sum_of_digits - int(nif[-1]))  % 11
        if (nif[-1] == '0' and (rest == 0 or rest ==1)):
            return nif
        elif nif[-1] == str(11- rest):
            return nif
        else:
            raise forms.ValidationError(message= "This is not a valid NIF")
    


class RawProductForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    height = forms.DecimalField(max_digits=3, decimal_places=2)
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    id_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Your id number'}))
    is_alive = forms.BooleanField(initial=True)

