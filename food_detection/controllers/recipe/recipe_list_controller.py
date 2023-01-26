from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from food_detection.models import Recipe

@login_required
def show(request):
    user_id = request.user.id
    recipes = Recipe.objects.filter(user_id=user_id)
    return render(request, 'views/recipe/recipes_list.html', {'recipes': recipes})
