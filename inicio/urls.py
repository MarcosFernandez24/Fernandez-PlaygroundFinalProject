from django.urls import path
from inicio.views import vista_principal, crear_personaje, personajes, ver_personaje, eliminar_personaje, editar_personaje

urlpatterns = [
    path('', vista_principal, name='inicio'),
    path('personajes/nuevo/', crear_personaje, name='crear_personaje'),
    path('personajes/', personajes, name='personajes'),
    path('personajes/int:<id_personaje>/', ver_personaje, name='ver_personaje'),
    path('personajes/int:<id_personaje>/eliminar/', eliminar_personaje, name='eliminar_personaje'),
    path('personajes/int:<id_personaje>/editar/', editar_personaje, name='editar_personaje'),
]
