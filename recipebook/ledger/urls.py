from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-creation'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view(), name='image-upload')
]

app_name = 'ledger'
