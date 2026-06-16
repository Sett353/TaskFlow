from django import forms
from .models import Miembro

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'estado_activo': forms.CheckboxInput(),
        }