from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recursos, name='lista_recursos'),
    path('eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
]