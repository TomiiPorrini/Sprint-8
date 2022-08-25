from unicodedata import name
from django import forms 
import datetime

tipo_prestamo = [
    ("PP","Prestamo_Personal"),
    ("PE","Prestamo_Estudiante"),
    ("PC","Prestamo_Comercios"),
    ("PH", "Prestamo_Hipotecario"),
] 

class createPrestamo(forms.Form):
    name = forms.CharField(label="nombre",widget=forms.TextInput(), required= True)
    last_name =forms.CharField(label="apellido",widget=forms.TextInput(), required= True)
    dni = forms.CharField(label="dni",widget=forms.TextInput() ,required=True)
    start_date = forms.DateField(initial=datetime.date.today, widget = forms.HiddenInput())
    valor = forms.CharField(label='valor del prestamo',widget=forms.TextInput(), required= True)
    loan_type = forms.CharField(label='tipo de prestamo',widget=forms.Select(choices=tipo_prestamo),required=True)
    loan_status= forms.BooleanField(label='estado del prestamo', initial= True, widget = forms.HiddenInput())
    
   