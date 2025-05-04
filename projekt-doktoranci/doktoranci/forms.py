from django import forms
from .models import PrzewodDoktorski

class PrzewodDoktorskiForm(forms.ModelForm):
    class Meta:
        model = PrzewodDoktorski
        fields = ['doktorant', 'temat', 'promotor']
