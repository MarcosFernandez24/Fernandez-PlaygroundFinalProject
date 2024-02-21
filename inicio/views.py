from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Personaje
import random
from inicio.forms import FormularioCrearPersonaje



def vista_principal(request): 
    template = loader.get_template('index.html')

    return render(request, 'index.html')
    
      
def personajes(request):
    
    personajes = Personaje.objects.all()
     
    return render(request, 'personajes.html', {'personajes': personajes})
      


def crear_personaje(request):
    
    formulario = FormularioCrearPersonaje()
    if request.method == "POST":
        formulario = FormularioCrearPersonaje(request.POST)
        if formulario.is_valid():
            personaje_nombre = formulario.cleaned_data.get('personaje_nombre')
            tipo_de_poder = formulario.cleaned_data.get('tipo_de_poder')
            daño_de_poder = formulario.cleaned_data.get('daño_de_poder')
            dmg_realizado = random.randint(5,  daño_de_poder)
            creacion_personaje = Personaje(personaje_nombre = personaje_nombre, tipo_de_poder = tipo_de_poder, daño_de_poder = daño_de_poder, dmg_realizado = dmg_realizado)
            creacion_personaje.save()
            return redirect("personajes")
   
    return render(request, 'crear_personaje.html', {'formulario': formulario})

