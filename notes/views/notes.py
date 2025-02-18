from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from notes.models.notes import Note
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




class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note/notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note/note_detail.html'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note/note_form.html'
    fields = ['title', 'content', 'category', 'tags', 'is_archived', 'is_favorite']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('note-list')

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/note/note_form.html'
    fields = ['title', 'content', 'category', 'tags', 'is_archived', 'is_favorite']
    success_url = reverse_lazy('note-list')

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')