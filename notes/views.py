from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Tag, Note
from django.contrib.auth.mixins import LoginRequiredMixin

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'notes/categories/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'notes/categories/category_form.html'
    fields = ['name']
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'notes/categories/category_form.html'
    fields = ['name']
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'notes/categories/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

# Tag Views
class TagListView(ListView):
    model = Tag
    template_name = 'tags/tag_list.html'
    context_object_name = 'tags'

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'tags/tag_form.html'
    fields = ['name']
    success_url = reverse_lazy('tag-list')

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'tags/tag_form.html'
    fields = ['name']
    success_url = reverse_lazy('tag-list')

class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tags/tag_confirm_delete.html'
    success_url = reverse_lazy('tag-list')

# Note Views
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content', 'category', 'tags', 'is_archived', 'is_favorite']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('note-list')

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content', 'category', 'tags', 'is_archived', 'is_favorite']
    success_url = reverse_lazy('note-list')

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')
