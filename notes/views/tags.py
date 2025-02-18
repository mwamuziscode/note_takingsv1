from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


# Tag Views
class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'notes/tags/tags_list.html'
    context_object_name = 'tags'

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'notes/tags/tags_form.html'
    fields = ['name']
    success_url = reverse_lazy('tag-list')

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'tags/tags_form.html'
    fields = ['name']
    success_url = reverse_lazy('tag-list')

class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'notes/tags/tags_confirm_delete.html'
    success_url = reverse_lazy('tag-list')

