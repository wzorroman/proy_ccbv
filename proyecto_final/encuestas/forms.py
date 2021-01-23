
from django import forms
from encuestas.models import Respuesta


class FormularioRespuesta(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ('pregunta', 'respuesta')
        

