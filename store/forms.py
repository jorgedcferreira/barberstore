from .models import Store
from django import forms

class StoreForm(forms.ModelForm): 

    class Meta:
        model = Store
        fields = [
            'name',
            'address',
            'zip_code'        
        ]
    
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'address': forms.TextInput(attrs={'class': 'form-control'}),
                'zip_code': forms.TextInput(attrs={'class': 'form-control'})
            }
