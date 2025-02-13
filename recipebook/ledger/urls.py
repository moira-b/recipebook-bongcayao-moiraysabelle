from django.urls import path
from .views import recipesList, recipe1, recipe2

urlpatterns = [
    # path('', index, name='index'),
    path('', recipesList, name='recipe-list'),
    path('recipes/list', recipesList, name='recipe-list'),
    path('recipe/1', recipe1, name='recipe-1'),
    path('recipe/2', recipe2, name='recipe-2'),
]

app_name = 'ledger'