from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .controllers import home_controller, sign_up_controller, login_controller, logout_controller
from .controllers.recipe import recipe_form_controller, recipe_list_controller, my_recipe_controller

urlpatterns = [
    #free
    path('', home_controller.show_ingredients_check, name='home'),
    path('sign_up/', sign_up_controller.show_sign_up, name='sign_up'),
    path('login/', login_controller.show_login, name='login'),

    #logged
    path('logout', logout_controller.disconnect, name='logout'),
    path('recipes_list/', recipe_list_controller.show, name='recipes_list'),
    path('recipe_form/', recipe_form_controller.show_create_recipe, name='recipe_form'),
    path('my_recipe/<int:recipe_id>/', my_recipe_controller.show, name='my_recipe'),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
