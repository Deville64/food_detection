from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from food_detection.forms import SignupForm

def show_sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']

            if password == password_confirmation:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Cet email est déjà utilisé')
                    return redirect('sign_up')

                else:
                    user = User.objects.create_user(
                        username= username,
                        email=email,
                        password=password
                    )
                    login(request, user)
                    messages.success(request, 'Vous êtes maintenant inscrit')
                    return redirect('home')
            else:
                messages.error(request, 'Les mots de passe ne correspondent pas')
                return redirect('sign_up')

    else:
        form = SignupForm()
    return render(request, 'views/sign_up.html', {'form': form})
