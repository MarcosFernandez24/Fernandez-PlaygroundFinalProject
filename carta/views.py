from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from carta.models import Carta
from django.urls import reverse_lazy 

class Cartas(ListView):
    model = Carta
    context_object_name = 'cartas'
    template_name = 'cartas/cartas.html'

class CrearCartas(CreateView):
    model = Carta
    template_name = "cartas/crear_cartas.html"
    fields = ['nombre_carta', 'elemento', 'daño_de_carta']
    success_url = reverse_lazy('cartas')
      
class EliminarCarta(DeleteView):
    model = Carta
    template_name = "cartas/eliminar_cartas.html"
    success_url = reverse_lazy('cartas')
    
    
class ModelUpdateView(UpdateView):
    model = Carta
    template_name = "cartas/editar_cartas.html"
    success_url = reverse_lazy('cartas')
    fields = ['nombre_carta', 'elemento', 'daño_de_carta']

class ModelDetailView(DetailView):
    model = Carta
    template_name = "cartas/detalle_cartas.html"
