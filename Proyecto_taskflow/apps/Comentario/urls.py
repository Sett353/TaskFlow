from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.comentario_list,
        name='comentario_list'
    ),

    path(
        'crear/',
        views.comentario_create,
        name='comentario_create'
    ),

    path(
        'editar/<int:pk>/',
        views.comentario_update,
        name='comentario_update'
    ),

    path(
        'eliminar/<int:pk>/',
        views.comentario_delete,
        name='comentario_delete'
    ),
]