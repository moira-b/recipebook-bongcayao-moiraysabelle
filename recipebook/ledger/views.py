from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Ingredient, Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipesList.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe.html"

def recipe_list(request):
    ctx = {"recipes": Recipe.objects.all()}
    return render(request, 'ledger/recipesList.html', ctx)

def recipe_details(request, pk):
    ctx = {"recipe": Recipe.objects.get(pk=pk)}
    return render(request, 'ledger/recipe.html', ctx)