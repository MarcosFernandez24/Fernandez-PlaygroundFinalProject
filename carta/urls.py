from django.urls import path 
from carta import views


urlpatterns = [
    path('cartas/', views.Cartas.as_view(), name='cartas'),
    path('cartas/nuevo/', views.CrearCartas.as_view(), name='crear_cartas'),
    path('cartas/<int:pk>/', views.ModelDetailView.as_view(), name='detalle_cartas'),
    path('cartas/<int:pk>/editar', views.ModelUpdateView.as_view(), name='editar_cartas'),
    path('cartas/<int:pk>/eliminar', views.EliminarCarta.as_view(), name='eliminar_cartas')
]
