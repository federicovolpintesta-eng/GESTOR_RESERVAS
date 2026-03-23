from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    repetir_4_semanas = forms.BooleanField(
        required=False, 
        label="Repetir semanalmente por un mes (4 semanas)"
    )

    class Meta:
        model = Reserva
        fields = ['recurso', 'inicio', 'fin', 'repetir_4_semanas']
        widgets = {
            'inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }