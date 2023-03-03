from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False)
    instructions = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preparation_time = models.CharField(max_length=20)
    cooking_time = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='enrolled')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
