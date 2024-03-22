from django import forms


class FormularioCrearPersonaje(forms.Form):
    personaje_nombre = forms.CharField(max_length=20)
    tipo_de_poder = forms.CharField(max_length=30)
    daño_de_poder = forms.IntegerField()
    
    
class BuscarHeroe(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
