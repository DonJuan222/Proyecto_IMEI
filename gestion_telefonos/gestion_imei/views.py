# gestion_imei/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from .models import Cell
from .forms import CellForm, CellEditForm, UserRegistrationForm

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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cell_list')
        else:
            return render(request, 'gestion_imei/login.html', {'error': 'Usuario o contraseña inválidos'})
    return render(request, 'gestion_imei/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            normal_user_group, created = Group.objects.get_or_create(name='NormalUser')
            user.groups.add(normal_user_group)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'gestion_imei/register.html', {'form': form})

@login_required
def cell_list(request):
    cells = Cell.objects.all()
    return render(request, 'gestion_imei/cell_list.html', {'cells': cells})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cell_create(request):
    if request.method == 'POST':
        form = CellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cell_list')
    else:
        form = CellForm()
    return render(request, 'gestion_imei/cell_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
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