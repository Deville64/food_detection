from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from food_detection.models import Recipe, Ingredient, RecipeIngredient
import shutil

@login_required
def show_create_recipe(request):
    if request.method == 'POST':
        if request.session['picture_path']:
            picture = shutil.move(request.session['picture_path'], 'media/enrolled/')
            
            del request.session['picture_path']
            del request.session['ingredients_list']

        else:
            picture = request.FILES.get('picture')

        name = request.POST.get('name')
        instructions = request.POST.get('instructions')
        preparation_time = request.POST.get('preparation_time')
        cooking_time = request.POST.get('cooking_time')

        recipe = Recipe.objects.create(
            picture = picture,
            name = name,
            instructions = instructions,
            preparation_time = preparation_time,
            cooking_time = cooking_time,
            user_id = request.user.id
        )
        recipe_id = recipe.id

        ingredients = request.POST.getlist('ingredients')
        quantity = request.POST.getlist('quantity')

        for i, ingredient_id in enumerate(ingredients):
            RecipeIngredient.objects.create(
                quantity=quantity[i],
                ingredient_id= ingredient_id,
                recipe_id=recipe_id
            )

        return redirect('my_recipe', recipe_id)
    else:
        ingredients = Ingredient.objects.values('id', 'name')
        return render(request, 'views/recipe/recipe_form.html', {'ingredients': ingredients})
