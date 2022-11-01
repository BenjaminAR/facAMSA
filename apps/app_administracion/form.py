from django import forms
from apps.app_administracion.models import Administracion_vehiculo, Pagos_vehiculo

class Agregar_vehiculo_form(forms.ModelForm):
    class Meta:
        model = Administracion_vehiculo
        fields = [
            'usuario',
            'empresa',
            'modelo',
            'año',
            'placa',
            'entidad',
            'vin',
        ]

        labels = {
            'usuario':'Usuario',
            'empresa':'Empresa',
            'modelo': 'Modelo',
            'año': 'Año',
            'placa': 'Placa',
            'entidad': 'Entidad',
            'vin': 'VIN',
        }

        widgets = {
            'usuario' : forms.Select(attrs={'class':'form-control'}),
            'empresa' : forms.Select(attrs={'class':'form-control', }),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'año':  forms.NumberInput(attrs={'class':'form-control'}), 
            'placa': forms.TextInput(attrs={'class':'form-control'}),
            'entidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado emisor de documentación'}),
            'vin' : forms.TextInput(attrs={'class':'form-control'}),
        }

class Agregar_pago_form(forms.ModelForm):
    class Meta:
        #exclude = ('date', )
        model = Pagos_vehiculo
        fields = [
            'vehiculo',
            'tenencia', 
            'costo_tenencia',
            'verificacion',
            'refrendo',
            'tarjeta_circulacion',
            'seguro',
            'costo_seguro', 
        ]

        labels = {
            'vehiculo':'Vehiculo ID',
            'tenencia': 'Tenencia', 
            'costo_tenencia':'Costo de la tenencia',
            'verificacion':'Verificación',
            'refrendo':'Refrendo',
            'tarjeta_circulacion':'Tarjeta de circualción',
            'seguro':'Seguro',
            'costo_seguro': 'Costo del seguro', 
        }

        widgets = {
            'vehiculo': forms.HiddenInput(attrs={'class':'form-control'}),
            'tenencia':  forms.DateInput(attrs={'class':'form-control'}), 
            'costo_tenencia': forms.NumberInput(attrs={'class':'form-control'}),
            'verificacion': forms.DateInput(attrs={'class':'form-control'}),
            'refrendo': forms.DateInput(attrs={'class':'form-control'}),
            'tarjeta_circulacion': forms.DateInput(attrs={'class':'form-control'}),
            'seguro': forms.DateInput(attrs={'class':'form-control'}),
            'costo_seguro': forms.NumberInput(attrs={'class':'form-control'}),
        }

class BookingForm(forms.Form):
    eventTitle = forms.CharField(label="event", max_length=255, required=True)
    startDateTime = forms.DateTimeField(label="startDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)
    endDateTime = forms.DateTimeField(label="endDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)

class Evento_form(forms.Form):
    eventTitle = forms.CharField(label="event", max_length=255, required=True)
    startDateTime = forms.DateTimeField(label="startDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)
    endDateTime = forms.DateTimeField(label="endDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)

