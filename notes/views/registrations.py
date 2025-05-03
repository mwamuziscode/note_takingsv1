# registration/register.html
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from faker import Faker





class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:login')  # Redirect to login page after registration
        return render(request, 'registration/register.html', {'form': form})
    


def logout_view(request):
    logout(request)
    return redirect('notes:login')  # Redirect to the login page after logout


