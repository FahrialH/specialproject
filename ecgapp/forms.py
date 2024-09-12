from django import forms
from .models import ECGFile

class ECGFileForm(forms.ModelForm):
    class Meta:
        model = ECGFile
        fields = ('file', )