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
    
    def get(self, request, *args, **kwargs):
        # Get the project slug from the URL
        slug = kwargs.get('slug')
        # Fetch the project object based on the slug
        project_Exist = get_object_or_404(Project, slug=slug)
        # Render the template with the project context
        return render(request, self.template_name, {'project': project_Exist})




class SummaryView(TemplateView):
    Model = Project
    template_name = 'norjiras/plannings/project_planning_summarys.html'
    context_object_name = 'project_sums'

    

class TimelineView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_timeline.html'


class BacklogView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_backlog.html'


class BoardView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_board.html'


class CalendarView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_calendar.html'

class TypeCreateView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_list.html'

class FormsView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_forms.html'

class GoalsView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_goals.html'    

class AllWorkView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_allwork.html'

class ReportsView(TemplateView):
    template_name = 'norjiras/plannings/project_planning_reports.html'


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

