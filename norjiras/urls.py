
from django.urls import path
from django.contrib.auth import views as auth_views
from notes.views import cats, tags, notes, profiles, index, registrations
from debug_toolbar.toolbar import debug_toolbar_urls
from norjiras.views import project
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


# Authentication URL

urlpatterns += [] + debug_toolbar_urls()
