from django import forms
from .models import hewan

class hewanform(forms.ModelForm):
    class Meta:
        model = hewan
        fields = ('nama', 'species', 'berat')
