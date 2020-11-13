from django import forms
from .models import *

class Register(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
