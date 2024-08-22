from django.shortcuts import render, HttpResponse

recipes = [

  {
    'author': 'Lamin',
    'title': 'Lasagna recipe',
    'instructions': 'put all the ingredients together',
    'date_posted': 'August 22, 2024'
  },
  {
    'author': 'Lady T',
    'title': 'Meat Balls recipe',
    'instructions': 'put all the ingredients together',
    'date_posted': 'August 22, 2024'
  },
  {
    'author': 'Alex',
    'title': 'Spaghetti Bolognese recipe',
    'instructions': 'put all the ingredients together',
    'date_posted': 'August 22, 2024'
  }
]
# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

def about(request):
    return render(request, "recipes/about.html",)