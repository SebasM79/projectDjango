from django.shortcuts import render, redirect
from .forms import LibroForm, EditorialForm

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')  # Redirige después de guardar
    else:
        form = LibroForm()
    return render(request, 'libro/crear_libro.html', {'form': form})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_editorial')  # Redirige después de guardar
    else:
        form = EditorialForm()
    return render(request, 'libro/crear_editorial.html', {'form': form})