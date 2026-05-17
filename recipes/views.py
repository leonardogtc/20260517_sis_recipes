from django.shortcuts import render


def home(request):
    # This is a placeholder view function
    return render(request, 'recipes/home.html', context={
        'name': 'Leonardo',
    })


def sobre(request):
    return render(request, 'recipes/sobre.html')


def contato(request):
    return render(request, 'recipes/contato.html')
