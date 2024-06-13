from django import forms 
from .models import *


class SchoolForms(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'