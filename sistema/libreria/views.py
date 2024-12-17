from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

#declarar funcion de solicitud a la aplicacion 
def inicio(request):
    #Imprime texto
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    #Busca archivo
    return render(request, 'paginas/nosotros.html')

def bin(request):
    #Busca el index
    return render(request, 'bin/index.html')

def crear(request):
    #Busca crear
    return render(request, 'bin/crear.html')

def editar(request):
    #Busca crear
    return render(request, 'bin/editar.html')