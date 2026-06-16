from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Miembro
from .forms import MiembroForm

@login_required
def lista_miembros(request):
    miembros = Miembro.objects.all()
    return render(request, 'miembro/lista.html', {'miembros': miembros})

@login_required
def agregar_miembro(request):
    form = MiembroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_miembros')
    return render(request, 'miembro/form.html', {'form': form})

@login_required
def editar_miembro(request, id):
    miembro = get_object_or_404(Miembro, id=id)
    form = MiembroForm(request.POST or None, instance=miembro)
    if form.is_valid():
        form.save()
        return redirect('lista_miembros')
    return render(request, 'miembro/form.html', {'form': form})

@login_required
def eliminar_miembro(request, id):
    miembro = get_object_or_404(Miembro, id=id)
    if request.method == 'POST':
        miembro.delete()
        return redirect('lista_miembros')
    return render(request, 'miembro/confirmar_eliminar.html', {'miembro': miembro})