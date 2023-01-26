from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from food_detection.forms import LoginForm

def show_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()
    return render(request, 'views/login.html', {'form': form})
