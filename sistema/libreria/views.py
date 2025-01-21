from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import bin
from .forms import binForm
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

#declarar funcion de solicitud a la aplicacion 
def inicio(request):
    #Imprime texto
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    #Busca archivo
    return render(request, 'paginas/nosotros.html')

#def listar_bin(request):
    # Cambia el nombre de la función para evitar conflicto
    bins = bin.objects.all()  # Corrige "objetcs" a "objects"
    return render(request, 'bin/index.html', {'bin': bins})

def bin_view(request):  # Cambia el nombre de la función para evitar conflictos con el modelo.
    registros = bin.objects.all()  # Usa un nombre diferente para la variable local.
    return render(request, 'bin/index.html', {'bin': registros})

def crear(request):
    #Busca crear
    formulario = binForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('bin')
    return render(request, 'bin/crear.html', {'formulario': formulario})


def editar(request, id):
    registro = get_object_or_404(bin, id=id)  # Obtén el objeto por su ID
    if request.method == 'POST':
        formulario = binForm(request.POST, request.FILES, instance=registro)  # Asocia el formulario al registro
        if formulario.is_valid():
            formulario.save()
            return redirect('bin')  # Redirige después de guardar
    else:
        formulario = binForm(instance=registro)  # Pasa el registro al formulario
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('bin') 
    return render(request, 'bin/editar.html', {'formulario': formulario})

#def editar(request,id):
    #Busca crear
    registro = bin.objects.get(id=id)    
    formulario = binForm(request.POST or None, request.FILES or None, instance=bin)
    return render(request, 'bin/editar.html', {'formulario': formulario})

#def eliminar(request, id):
    #Busca crear
    registro = bin.objects.get(id=id)
    bin.delete()
    return render(request, 'bin')

def eliminar(request, id):
    # Obtener la instancia del objeto o lanzar un error 404 si no existe
    registro = get_object_or_404(bin, id=id)
    
    # Eliminar el objeto
    registro.delete()
    
    # Redirigir después de la eliminación
    return redirect('bin')  # Cambia 'bin' por el nombre de tu vista de lista