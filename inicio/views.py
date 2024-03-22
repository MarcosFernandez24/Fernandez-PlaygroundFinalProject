from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Personaje
import random
from inicio.forms import FormularioCrearPersonaje, BuscarHeroe



def vista_principal(request): 
    template = loader.get_template('inicio/index.html')

    # return render(request, 'inicio/index.html')
    return render(request, "inicio/index.html")
    
      
def personajes(request):
    
    personajes = Personaje.objects.all()
    formulario = BuscarHeroe(request.GET)
    if formulario.is_valid():
        info_busqueda = formulario.cleaned_data.get('nombre')
        personajes = Personaje.objects.filter(personaje_nombre__icontains =  info_busqueda)
        
    return render(request, 'inicio/personajes.html', {'personajes': personajes, 'formulario': formulario})
      


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
   
    return render(request, 'inicio/crear_personaje.html', {'formulario': formulario})

def eliminar_personaje (request):
    ... 

def editar_personaje(requuest):
    ...

def ver_personaje(request, id_personaje):
    personaje = Personaje.objects.get(id=id_personaje)
    return render(request, 'inicio/ver_personaje.html', {'personaje' : personaje})
