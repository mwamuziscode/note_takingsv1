from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from norjiras.models.project_models import Project, IssueType #, ProjectCategory, ProjectLead
from django.shortcuts import render
from django.views import View

class PlanningDashboardView(View):
    template_name = 'norjiras/plannings/project_planning_dashboard.html'
    
    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context



class SummaryView(TemplateView):
    Model = Project
    template_name = 'norjiras/plannings/project_planning_summarys.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context

    

class TimelineView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_timeline.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context

class BacklogView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_backlog.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context



class BoardView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_board.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context




class CalendarView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_calendar.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context
class TypeCreateView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_list.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context
    



class FormsView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_forms.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context
    


class GoalsView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_goals.html'    
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context
    

class AllWorkView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_allwork.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context
    

class ReportsView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_reports.html'
    context_object_name = 'project'

    #get the project slug from the URL
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Add the project to the context
        context['project'] = project_Exist
        return context

 



class TypeCreateView(LoginRequiredMixin, CreateView):
    model = IssueType
    template_name = 'norjiras/plannings/project_planning_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('norjiras:type-list')



class TypeView(TemplateView):
    model = IssueType
    template_name = 'norjiras/plannings/project_planning_List.html'
    fields = '__all__'
    context_object_name = 'issue_types'
    success_url = reverse_lazy('norjiras:type-list')

