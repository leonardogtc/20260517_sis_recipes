from django.http import HttpResponse
from django.urls import path
from django.contrib import admin


def my_view(request):
    # This is a placeholder view function
    return HttpResponse("This is the 'sobre' page.")


def sobre(request):
    return HttpResponse(request, 'sobre.html')


def contato(request):
    return HttpResponse(request, 'contato.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view, name='sobre'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='sobre'),
]
