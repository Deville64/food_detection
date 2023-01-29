from django.shortcuts import render,redirect
from food_detection.models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def show(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipeingredients= recipe.recipeingredient_set.all()
    if recipe.user_id == request.user.id:
        return render(request, 'views/recipe/my_recipe.html', {'recipe': recipe, 'recipeingredients': recipeingredients})
    else:
        redirect('recipes_list')
