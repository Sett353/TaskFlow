from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm

# Create your views here.
def comentario_list(request):

    comentarios = Comentario.objects.all()

    total_comentarios = comentarios.count()

    visibles = comentarios.filter(
        visibilidad_cliente=True
    ).count()

    editados = comentarios.filter(
        editado=True
    ).count()

    return render(
        request,
        'comentario/listar.html',
        {
            'comentarios': comentarios,
            'total_comentarios': total_comentarios,
            'visibles': visibles,
            'editados': editados
        }
    )
    
def comentario_create(request):

    if request.method == 'POST':

        form = ComentarioForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'comentario_list'
            )

    else:

        form = ComentarioForm()

    return render(
        request,
        'comentario/comentario_form.html',
        {'form': form}
    )
    
def comentario_update(request, pk):

    comentario = get_object_or_404(
        Comentario,
        pk=pk
    )

    if request.method == 'POST':

        form = ComentarioForm(
            request.POST,
            request.FILES,
            instance=comentario
        )

        if form.is_valid():

            comentario = form.save(
                commit=False
            )

            comentario.editado = True

            comentario.save()

            return redirect(
                'comentario_list'
            )

    else:

        form = ComentarioForm(
            instance=comentario
        )

    return render(
        request,
        'comentario/comentario_form.html',
        {'form': form}
    )

def comentario_delete(request, pk):

    comentario = get_object_or_404(
        Comentario,
        pk=pk
    )

    if request.method == 'POST':

        comentario.delete()

        return redirect(
            'comentario_list'
        )

    return render(
        request,
        'comentario/comentario_confirm_delete.html',
        {'comentario': comentario}
    )
    
