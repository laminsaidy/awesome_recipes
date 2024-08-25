from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


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

class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'

class RecipeDetailView(DetailView):
  model = models.Recipe

class RecipeCreateView(CreateView):
  model = models.Recipe
  fields = ['title', 'description']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  fields = ['title', 'description']

  def test_func(self):
     
    recipe = self.get_object()
    return self.request.user == recipe.author

  
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  

def about(request):
    return render(request, 'recipes/about.html', {'title': 'about page'})