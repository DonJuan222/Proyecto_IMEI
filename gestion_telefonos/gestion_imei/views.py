# gestion_imei/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cell
from .forms import CellForm, CellEditForm

def cell_list(request):
    cells = Cell.objects.all()
    return render(request, 'gestion_imei/cell_list.html', {'cells': cells})

def cell_create(request):
    if request.method == 'POST':
        form = CellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cell_list')
    else:
        form = CellForm()
    return render(request, 'gestion_imei/cell_form.html', {'form': form})

def cell_edit(request, pk):
    cell = get_object_or_404(Cell, pk=pk)
    if request.method == 'POST':
        form = CellEditForm(request.POST, instance=cell)
        if form.is_valid():
            form.save()
            return redirect('cell_list')
    else:
        form = CellEditForm(instance=cell)
    return render(request, 'gestion_imei/cell_form.html', {'form': form, 'edit': True})
