from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from norjiras.models.project_models import Project, IssueType, Issue #, ProjectCategory, ProjectLead
from django.shortcuts import render
from django.views import View



# IssueType
class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'norjiras/plannings/project_planning_List.html'
    context_object_name = 'issue_types'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context


