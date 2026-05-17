from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # This is a placeholder view function
    return HttpResponse("Página principal do seu aplicativo.")


def sobre(request):
    return HttpResponse('sobre.html')


def contato(request):
    return HttpResponse('contato.html')
