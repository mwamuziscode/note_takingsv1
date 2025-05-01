from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from norjiras.models import  Project
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


from faker import Faker


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'norjiras/project/projects_list.html'
    context_object_name = 'project'
    #success_url = reverse_lazy('norjiras:project-list')


class ProjectDetailView(View):
    def get(self, request, pk):
        note = get_object_or_404(Project, pk=pk)
        template_name = 'norjiras/project/project_detail.html'
        return render(request, template_name, {'note': note})

    def post(self, request, pk):
        note = get_object_or_404(Project, pk=pk)
        note.delete()
        return redirect('note-list')  # Redirect to a list of notes or wherever you want after delete



# NoteForm 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'norjiras/project/project_form.html'
    fields = '__all__'
    success_url = reverse_lazy('norjiras:project-list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'norjiras/project/project_form.html'
    fields = '__all__'
    success_url = reverse_lazy('norjiras:project-list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'norjiras/project/project_confirm_delete.html'
    success_url = reverse_lazy('norjiras:project-list')

