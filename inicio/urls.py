from django.urls import path
from inicio.views import vista_principal, crear_personaje, personajes

urlpatterns = [
    path('', vista_principal, name='inicio'),
    path('personajes/nuevo/', crear_personaje, name='crear_personaje'),
    path('personajes/', personajes, name='personajes'),
]
