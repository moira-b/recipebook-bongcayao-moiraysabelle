from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('ledger:ingredient',args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('ledger:recipe',args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredientType = models.ForeignKey(Ingredient,on_delete=models.CASCADE,related_name='recipe',)
    inRecipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name='ingredients',)
