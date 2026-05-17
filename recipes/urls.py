# Arquivo urls.py da aplicação "recipes"
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
