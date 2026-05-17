from django.http import HttpResponse
from django.urls import path
from django.contrib import admin


def home(request):
    # This is a placeholder view function
    return HttpResponse("Página principal do seu aplicativo.")


def sobre(request):
    return HttpResponse(request, 'sobre.html')


def contato(request):
    return HttpResponse(request, 'contato.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='sobre'),
]
