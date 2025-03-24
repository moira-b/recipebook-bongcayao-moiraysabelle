from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])

    author = models.CharField(max_length=100, default="Anonymous")
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient_Type = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='recipe',
    )
    in_Recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients',
    )
    
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.TextField(max_length=255)
    image_in_Recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="images",
    )

