from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ingredient',args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('recipe',args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.DecimalField(decimal_places=2, max_digits = 10) # real-life recipes will generally not need to exceed these parameters
    ingredientType = models.ForeignKey(Ingredient, 
                                       on_delete=models.CASCADE, 
                                       related_name='recipe')
    inRecipe = models.ForeignKey(Recipe, 
                                 on_delete=models.CASCADE, 
                                 related_name='ingredients')