from django import forms
from .models import bin

class binForm(forms.ModelForm):
    class Meta:
        model = bin
        fields = '__all__'