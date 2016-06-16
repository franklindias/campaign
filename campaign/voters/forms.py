from datetime import date

from django import forms
from django.contrib.admin import widgets   
from .models import *

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ['id', 'cityVoting', 'stateVoting']
        fields = ('__all__')
        widgets = { 'dataNascimento': forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'placeholder':'dd/MM/AAAA'}),
        			'dataNascimento': forms.DateInput(attrs={'class':''}),
         #   'ano_letivo': forms.NumberInput(attrs={'class': 'form-control', 'aria-required':'true'}),
          #  'unit': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'})

        }