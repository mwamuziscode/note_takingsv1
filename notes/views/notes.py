from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from notes.models.notest import Note
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
from django import forms

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note/notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteDetailView(View):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        template_name = 'notes/note/note_detail.html'
        return render(request, template_name, {'note': note})

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return redirect('notes:note-list')  # Redirect to a list of notes or wherever you want after delete



# NoteForm 
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        #fields = '__all__'
        fields = [
            'title', 
            'image_name', 
            'picture_url', 
            'content', 
            'category', 
            'tags', 
            'is_archived', 
            'is_favorite'
        ]


def NoteCreateView(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:note-list')  # or use reverse_lazy if needed
    else:
        form = NoteForm()
    return render(request, 'notes/note/note_form.html', {'form': form})


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/note/note_form.html'
    fields = '__all__'
    success_url = reverse_lazy("notes:note-list")



class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note-list')

