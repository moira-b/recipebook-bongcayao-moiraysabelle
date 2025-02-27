from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

# class IngredientAdmin(admin.ModelAdmin):
#     model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine]

# class RecipeIngredientAdmin(admin.ModelAdmin):
#     model = RecipeIngredient

# admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(RecipeIngredient, RecipeIngredientAdmin)