from datetime import date

from django import forms
from .models import *

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ['id']
        fields = ('__all__')