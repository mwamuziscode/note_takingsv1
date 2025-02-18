from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from notes.models.notes import Note
from notes.models.cats import Category
from notes.models.tag import Tag
from django.contrib.auth.mixins import LoginRequiredMixin
# login_required decorator
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404

from faker import Faker

#import User
from django.contrib.auth.models import User
# Create your views here.




def index(request):
    return render(request, 'notes/index.html')


def custom_404_view(request, exception):
    return render(request, '404.html', {'request_path': request.path}, status=404)



#reset password
class PasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')





class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
        return render(request, 'registration/register.html', {'form': form})

# 
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout





# profile class view
class ProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, 'registration/profile.html', {'user': user})






def createNote():
    fake = Faker()
    for _ in range(10):
        category = Category.objects.create(name=fake.word())
        tag = Tag.objects.create(name=fake.word())
        note = Note.objects.create(
            title=fake.sentence(),
            content=fake.text(),
            picture= "https://loremflickr.com/320/240",
            category=category,
            is_archived=fake.boolean(chance_of_getting_true=50),
            user= User.objects.filter(is_superuser=True).order_by('?').first()
        )
        note.tags.add(tag)
        note.save()
    return 'Fake data created successfully'

# createNote()



# DELETE ALL TAGS AND CATEGORIES
def DeleteAll():
   def deleteAllTags():
    Tag.objects.all().delete()
    return 'All Tags deleted successfully'

   def deleteAllCategories():
    Category.objects.all().delete()
    return 'All Categories deleted successfully'

   def deleteAllNotes():
    Note.objects.all().delete()
    return 'All Notes deleted successfully'

   deleteAllTags()
   deleteAllCategories()
   deleteAllNotes()

# DeleteAll()