from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, world! utilizando Django.</h1>")

def seba(request):
    return HttpResponse("<h1>Hola, soy Sebas.</h1>")
def home(request):
    return HttpResponse( 'hice otra direccion para saber si funciona')
def about(request):
    return HttpResponse("<h1>Esta es la pagina de about.</h1>")