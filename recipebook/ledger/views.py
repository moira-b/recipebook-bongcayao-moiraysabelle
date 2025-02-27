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

# def recipesList(request):
#     recipeListCtx = {        
#         "recipes": [
#             {
#                 "name": "Recipe 1",
#                 "ingredients": [
#                     {
#                         "name": "tomato",
#                         "quantity": "3pcs"
#                     },
#                     {
#                         "name": "onion",
#                         "quantity": "1pc"
#                     },
#                     {
#                         "name": "pork",
#                         "quantity": "1kg"
#                     },
#                     {
#                         "name": "water",
#                         "quantity": "1L"
#                     },
#                     {
#                         "name": "sinigang mix",
#                         "quantity": "1 packet"
#                     }
#                 ],
#                 "link": "/recipe/1"
#             },
#             {
#                 "name": "Recipe 2",
#                 "ingredients": [
#                     {
#                         "name": "garlic",
#                         "quantity": "1 head"
#                     },
#                     {
#                         "name": "onion",
#                         "quantity": "1pc"
#                     },
#                     {
#                         "name": "vinegar",
#                         "quantity": "1/2cup"
#                     },
#                     {
#                         "name": "water",
#                         "quantity": "1 cup"
#                     },
#                     {
#                         "name": "salt",
#                         "quantity": "1 tablespoon"
#                     },
#                     {
#                         "name": "whole black peppers",
#                         "quantity": "1 tablespoon"
#                     },
#                     {
#                         "name": "pork",
#                         "quantity": "1 kilo"
#                     }
#                 ],
#                 "link": "/recipe/2"
#             }
#         ]
#     }

#     return render(request, 'recipesList.html', recipeListCtx)

# def recipe1(request):
#     recipe1Ctx = {
#         "name": "Recipe 1",
#         "ingredients": [
#             {
#                 "name": "tomato",
#                 "quantity": "3pcs"
#             },
#             {
#                 "name": "onion",
#                 "quantity": "1pc"
#             },
#             {
#                 "name": "pork",
#                 "quantity": "1kg"
#             },
#             {
#                 "name": "water",
#                 "quantity": "1L"
#             },
#             {
#                 "name": "sinigang mix",
#                 "quantity": "1 packet"
#             }
#         ],
#         "link": "/recipe/1"
#     }

#     return render(request, 'recipe.html', recipe1Ctx)

# def recipe2(request): 
#     recipe2Ctx = {
#         "name": "Recipe 2",
#         "ingredients": [
#             {
#                 "name": "garlic",
#                 "quantity": "1 head"
#             },
#             {
#                 "name": "onion",
#                 "quantity": "1pc"
#             },
#             {
#                 "name": "vinegar",
#                 "quantity": "1/2cup"
#             },
#             {
#                 "name": "water",
#                 "quantity": "1 cup"
#             },
#             {
#                 "name": "salt",
#                 "quantity": "1 tablespoon"
#             },
#             {
#                 "name": "whole black peppers",
#                 "quantity": "1 tablespoon"
#             },
#             {
#                 "name": "pork",
#                 "quantity": "1 kilo"
#             }
#         ],
#         "link": "/recipe/2"
#     }

#     return render(request, 'recipe.html', recipe2Ctx)