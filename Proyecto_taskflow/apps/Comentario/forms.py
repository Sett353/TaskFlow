from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):

    class Meta:

        model = Comentario

        fields = [
            'tarea',
            'autor',
            'texto_comentario',
            'archivo_adjunto',
            'visibilidad_cliente'
        ]