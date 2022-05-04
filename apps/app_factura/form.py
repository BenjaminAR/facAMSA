from django import forms
from apps.app_factura.models import Solicitud, Solicitud_atendida
    
class solicitud(forms.ModelForm):

    class Meta:
        exclude = ('solicito',)
        model = Solicitud
        fields = [
            'sucursal',
            'documento',
            'nombre_cliente',
            'cartera_cliente',
            'numOrden',
            'folio',
            'rfc',
            'cuenta_contable',
            'motivo_de_cancelacion',
            'fecha_sol_de_cancelacion',
            'obs',
        ]
        labels = {
            'sucursal':'Empresa', 
            'documento':'Documento',
            'nombre_cliente':'Nombre del cliente',
            'cartera_cliente':'Cartera de cliente',
            'numOrden': 'Número de orden/Inventario',
            'folio': 'Folio',
            'rfc': 'RFC',
            'cuenta_contable':'Cuenta contable',
            'motivo_de_cancelacion': 'Motivo de cancelación',
            'fecha_sol_de_cancelacion': 'Fecha de la solicitud de cancelación',
            'obs': 'Observaciones',
        }

        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control'}), 
            'documento': forms.Select(attrs={'class':'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'cartera_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'numOrden': forms.NumberInput(attrs={'class':'form-control'}),
            'folio': forms.NumberInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta_contable':forms.TextInput(attrs={'class':'form-control'}),
            'motivo_de_cancelacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_sol_de_cancelacion': forms.DateInput(attrs={'class':'form-control'}),
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
            
            'atendida': forms.HiddenInput(attrs={'class':'form-control'}),
            'fecha_de_cancelacion':  forms.DateInput(attrs={'class':'form-control'}), 
            'estatus': forms.TextInput(attrs={'class':'form-control disabled'}),
            'comentarios': forms.Textarea(attrs={'class':'form-control pad'}),
        }
