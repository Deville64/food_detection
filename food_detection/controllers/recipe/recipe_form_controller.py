from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from food_detection.forms import RecipeForm

@login_required
def show_create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes_list')
    else:
        form = RecipeForm()
    return render(request, 'views/recipe/recipe_form.html', {'form': form})
