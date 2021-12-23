from django import forms
from apps.app_factura.models import Solicitud, Solicitud_atendida
    
class solicitud(forms.ModelForm):

    class Meta:
        exclude = ('solicito',)
        model = Solicitud
        fields = [
            'sucursal',
            'area',
            'numOrden',
            'uid',
            'rfc',
            'folio',
            'fecha_sol_de_cancelacion',
            'motivo_de_cancelacion',
            'obs',
        ]
        labels = {
            'sucursal':'Empresa', 

            'area': 'Area',
            'numOrden': 'Número de orden',
            'uid': 'UUID',
            'rfc': 'RFC',
            'folio': 'Folio',
            'fecha_sol_de_cancelacion': 'Fecha de sol de cancelación',
            'motivo_de_cancelacion': 'Motivo de cancelación',
            'obs': 'Observaciones',
        }

        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control'}), 
            'area': forms.TextInput(attrs={'class':'form-control' ' disabled'}),
            'numOrden': forms.TextInput(attrs={'class':'form-control'}),
            'uid': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'folio': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_sol_de_cancelacion': forms.DateInput(attrs={'class':'form-control'}),
            'motivo_de_cancelacion': forms.TextInput(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control pad'}),
        }#etiquetas HTML


class atencion(forms.ModelForm):

    class Meta:
        exclude = ('date',)
        model = Solicitud_atendida
        fields = [
            'atendida',
            'fecha_de_cancelacion',
            'estatus',
            'comentarios',
        ]
        labels = {
            'atendida': 'id atendida',
            'fecha_de_cancelacion': 'Fecha de cancelación',
            'estatus': 'Estatus',
            'comentarios': 'Comentarios',

        }

        widgets = {
            'atendida': forms.TextInput(attrs={'class':'form-control' ' disabled'}),
            'fecha_de_cancelacion':  forms.DateInput(attrs={'class':'form-control'}), 
            'estatus': forms.TextInput(attrs={'class':'form-control' ' disabled'}),
            'comentarios': forms.Textarea(attrs={'class':'form-control pad'}),
        }
