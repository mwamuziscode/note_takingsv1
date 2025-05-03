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
from django.db.models import Q
from norjiras.models.project_models import Category

from faker import Faker




class ProjectDetailView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        template_name = 'norjiras/project/project_detail.html'
        return render(request, template_name, {'project': project})

    def post(self, request, pk):
        note = get_object_or_404(Project, pk=pk)
        note.delete()
        return redirect('notes:project-list')  # Redirect to a list of notes or wherever you want after delete



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


class ProjectListView(ListView):
    model = Project
    template_name = 'norjiras/project/projects_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category', 'project_lead').prefetch_related('project_members')
        search = self.request.GET.get('search', '')
        categories = self.request.GET.getlist('category')  # multiple categories
        status = self.request.GET.get('status', '')  # optional filter by project status

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(project_key__icontains=search)
            )

        if categories:
            queryset = queryset.filter(category__id__in=categories)

        if status:
            queryset = queryset.filter(project_status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['statuses'] = Project._meta.get_field('project_status').choices
        return context
