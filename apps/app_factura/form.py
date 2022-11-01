from faulthandler import disable
from django import forms
from apps.app_factura.models import NotaCargo, Vehiculo, Solicitud, Solicitud_atendida
    
class Solicitud_form(forms.ModelForm):

    class Meta:
        exclude = ('solicitante',)
        model = Solicitud
        fields = [
            #'solicitante',
            'sucursal',
            'nombre_cliente',
            'cartera_cliente',
            'folio',
            'UUID',
            'rfc',
            'motivo_de_cancelacion',
            'fecha_sol_de_cancelacion',
            #'obs',
        ]
        labels = {
            #'solicitante':'Solicita',
            'sucursal':'Empresa', 
            'nombre_cliente':'Nombre del cliente',
            'cartera_cliente':'Cartera de cliente',
            'folio': 'Folio',
            'UUID':'UUID/Folio fiscal',
            'rfc': 'RFC',
            'motivo_de_cancelacion': 'Motivo de cancelación',
            'fecha_sol_de_cancelacion': 'Fecha de la solicitud de cancelación',
            #'obs': 'Observaciones',
        }

        widgets = {
            #'solicitante': forms.Select(attrs={'class':'form-control', 'disabled':''}),
            'sucursal': forms.Select(attrs={'class':'form-control'}), 
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'cartera_cliente':forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'folio': forms.NumberInput(attrs={'class':'form-control'}),
            'UUID': forms.TextInput(attrs={'class':'form-control','placeholder': '00000000-0000-0000-0000-00000000000 escribir guiones','style':'text-transform: uppercase;' }),
            'rfc': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'motivo_de_cancelacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_sol_de_cancelacion': forms.DateInput(attrs={'class':'form-control'}),
            #'obs': forms.Textarea(attrs={'class':'form-control pad'}),
            
        }#etiquetas HTML

class Solicitud_nota_cargo_form(forms.ModelForm):
    
    class Meta:
        exclude = ('solicitante','documento', 'fecha_sol_de_cancelacion')
        model = NotaCargo
        fields = [
            #'solicitante',
            'sucursal',
            'nombre_cliente',
            'cartera_cliente',
            'folio',
            'rfc',
            'UUID',
            'motivo_de_cancelacion',
            'fecha_sol_de_cancelacion',
            'cuenta_contable',
            'archivo',
            'obs',
        ]
        labels = {
            #'solicitante':'Solicita',
            'sucursal':'Empresa', 
            'nombre_cliente':'Nombre del cliente',
            'cartera_cliente':'Cartera de cliente',
            'folio': 'Folio',
            'rfc': 'RFC del cliente',
            'UUID':'UUID/Folio fiscal',
            'motivo_de_cancelacion': 'Motivo de cancelación',
            'fecha_sol_de_cancelacion': 'Fecha de la solicitud de cancelación',
            'cuenta_contable':'Cuenta contable',
            'archivo':'PDF Generado por autoline',
            'obs': 'Observaciones',
        }

        widgets = {
            #'solicitante': forms.Select(attrs={'class':'form-control', 'disabled':''}),
            'sucursal': forms.Select(attrs={'class':'form-control'}), 
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'cartera_cliente':forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'cuenta_contable':forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'rfc': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'folio': forms.NumberInput(attrs={'class':'form-control'}),
            'UUID': forms.TextInput(attrs={'class':'form-control','placeholder': '00000000-0000-0000-0000-00000000000 escribir guiones','style':'text-transform: uppercase;' }),
            'motivo_de_cancelacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_sol_de_cancelacion': forms.DateInput(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control pad'} ),
            
        }

class Vehiculo_form(forms.ModelForm):
    class Meta:
        exclude = ('solicitante','fecha_sol_de_cancelacion')
        model = Vehiculo
        fields = [
            'sucursal',
            'nombre_cliente',
            'cartera_cliente',
            'folio',
            'rfc',
            'UUID',
            'motivo_de_cancelacion',
            'fecha_sol_de_cancelacion',
            'inv',
            'suplementaria',
            'archivo',
            'obs',
        ]
        labels = {
            'sucursal':'Empresa', 
            'nombre_cliente':'Nombre del cliente',
            'cartera_cliente':'Cartera de cliente',
            'rfc': 'RFC del cliente',
            'folio': 'Folio',
            'UUID':'UUID/Folio fiscal',
            'motivo_de_cancelacion': 'Motivo de cancelación',
            'fecha_sol_de_cancelacion': 'Fecha de la solicitud de cancelación',
            'inv':'Inventario de vehículo nuevo:',
            'suplementaria':'Suplementaria',
            'archivo':'PDF Generado por autoline',
            'obs': 'Observaciones',
        }
        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control'}), 
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'cartera_cliente':forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'rfc': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'folio': forms.NumberInput(attrs={'class':'form-control'}),
            'UUID': forms.TextInput(attrs={'class':'form-control','placeholder': '00000000-0000-0000-0000-00000000000 escribir guiones','style':'text-transform: uppercase;' }),
            'motivo_de_cancelacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_sol_de_cancelacion': forms.DateInput(attrs={'class':'form-control'}),
            'inv': forms.NumberInput(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control pad'} ),
            
        }#etiquetas HTML
    archivo = forms.FileField()
    archivo.widget.attrs.update({'class': 'form-control'})

class Vehiculo_seminuevo_form(forms.ModelForm):
    class Meta:
        exclude = ('solicitante','fecha_sol_de_cancelacion')
        model = Vehiculo
        fields = [
            'sucursal',
            'nombre_cliente',
            'cartera_cliente',
            'folio',
            'rfc',
            'UUID',
            'motivo_de_cancelacion',
            'fecha_sol_de_cancelacion',
            'inv',
            'suplementaria',
            'archivo',
            'obs',
        ]
        labels = {
            'sucursal':'Empresa', 
            'nombre_cliente':'Nombre del cliente',
            'cartera_cliente':'Cartera de cliente',
            'rfc': 'RFC del cliente',
            'folio': 'Folio',
            'UUID':'UUID/Folio fiscal',
            'motivo_de_cancelacion': 'Motivo de cancelación',
            'fecha_sol_de_cancelacion': 'Fecha de la solicitud de cancelación',
            'inv':'Inventario de vehículo nuevo:',
            'suplementaria':'Suplementaria',
            'archivo':'PDF Generado por autoline',
            'obs': 'Observaciones',
        }
        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control'}), 
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'cartera_cliente':forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'rfc': forms.TextInput(attrs={'class':'form-control','style':'text-transform: uppercase;'}),
            'folio': forms.NumberInput(attrs={'class':'form-control'}),
            'UUID': forms.TextInput(attrs={'class':'form-control','placeholder': '00000000-0000-0000-0000-00000000000 escribir guiones','style':'text-transform: uppercase;' }),
            'motivo_de_cancelacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_sol_de_cancelacion': forms.DateInput(attrs={'class':'form-control'}),
            'inv': forms.NumberInput(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control pad'} ),
        }
    archivo = forms.FileField()
    archivo.widget.attrs.update({'class': 'form-control'})
    suplementaria = forms.BooleanField()
    suplementaria.widget.attrs.update({'class': 'form-check-input form-control'})


class Solicitud_atendia_form(forms.ModelForm):

    class Meta:
        exclude = ('date', )
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

