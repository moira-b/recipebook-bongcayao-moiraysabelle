from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine, RecipeImageInLine]

admin.site.register(Recipe, RecipeAdmin)

### PERCHANCE DELETE AFTER ###

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

admin.site.register(Ingredient, IngredientAdmin)
