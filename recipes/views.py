from django.shortcuts import render, HttpResponse
from . import models

recipes =[
    {
    'author': 'Lamin',
    'title': 'Mafe',
    'directions': 'Combine groundnuts with meat',
    'date_posted': 'August 24, 2024'
    },
    {
    'author': 'Lex',
    'title': 'Meatballs',
    'directions': 'Soak the bread',
    'date_posted': 'August 28, 2024'

    },
    {
    'author': 'Yasin',
    'title': 'Omelette',
    'directions': 'Combine eggs with tomatos',
    'date_posted': 'August 30, 2024'

    },
]

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes 
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html', {'title': 'about page'})