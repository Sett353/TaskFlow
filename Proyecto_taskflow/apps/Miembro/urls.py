from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_miembros, name='lista_miembros'),
    path('agregar/', views.agregar_miembro, name='agregar_miembro'),
    path('editar/<int:id>/', views.editar_miembro, name='editar_miembro'),
    path('eliminar/<int:id>/', views.eliminar_miembro, name='eliminar_miembro'),
]