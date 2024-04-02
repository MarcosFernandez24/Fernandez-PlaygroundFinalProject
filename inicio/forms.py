from django import forms

class FormularioBasePersonaje(forms.Form):
    personaje_nombre = forms.CharField(max_length=20)
    tipo_de_poder = forms.CharField(max_length=30)
    daño_de_poder = forms.IntegerField()

class FormularioCrearPersonaje(FormularioBasePersonaje):
    ...
    

class FormularioEdicionPersonaje(FormularioBasePersonaje):
    personaje_nombre = forms.CharField(max_length=20)
    
    
    
class BuscarHeroe(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
