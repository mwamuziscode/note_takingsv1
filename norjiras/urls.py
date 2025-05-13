
from django.urls import path
from django.contrib.auth import views as auth_views
from notes.views import cats, tags, notes, profiles, index, registrations
from debug_toolbar.toolbar import debug_toolbar_urls
from norjiras.views import project, project_planning_dashboardViews
from django.urls import path

app_name = 'norjiras'

# notes pattrns
urlpatterns = [
    path('', project.ProjectListView.as_view(), name='project-list'),
    path('project/new/', project.ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/edit/', project.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', project.ProjectDeleteView.as_view(), name='project-delete'),
    path('project/<int:pk>/detail/', project.ProjectDetailView.as_view(), name='project-detail'),
]


# plannings patterns
urlpatterns += [ 
    path('<slug:slug>/', project_planning_dashboardViews.PlanningDashboardView.as_view(), name='planhboard'),
    #path('/<slug:slug>/plans-boroad/?section=backlog', project_planning_dashboardViews.PlanningDashboardView.as_view(), name='planning-dashboard-backlog'),
    path('<slug:slug>/summary/', project_planning_dashboardViews.SummaryView.as_view(), name='summary'),
    path('<slug:slug>/timeline/', project_planning_dashboardViews.TimelineView.as_view(), name='timeline'),
    path('<slug:slug>/backlog/', project_planning_dashboardViews.BacklogView.as_view(), name='backlog'),
    path('<slug:slug>/board/', project_planning_dashboardViews.BoardView.as_view(), name='board'),
    path('<slug:slug>/calendar/', project_planning_dashboardViews.CalendarView.as_view(), name='calendar'),
    path('<slug:slug>/plans-list/', project_planning_dashboardViews.TypeView.as_view(), name='type-list'),
    path('<slug:slug>/forms/', project_planning_dashboardViews.FormsView.as_view(), name='type-forms'),
    path('<slug:slug>/goals/', project_planning_dashboardViews.GoalsView.as_view(), name='goals'),
    path('<slug:slug>/all-work/', project_planning_dashboardViews.AllWorkView.as_view(), name='allwork'),
    path('<slug:slug>/reports/', project_planning_dashboardViews.ReportsView.as_view(), name='reports'),
]

urlpatterns += [] + debug_toolbar_urls()
