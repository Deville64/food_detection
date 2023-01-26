from django import forms
from .models import Recipe

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), required=True)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['picture', 'name', 'instructions', 'preparation_time', 'cooking_time']
