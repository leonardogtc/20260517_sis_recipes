from django.shortcuts import render


def home(request):
    # This is a placeholder view function
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Leonardo',
    })
