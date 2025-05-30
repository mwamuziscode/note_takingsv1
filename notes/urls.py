
from django.urls import path
from django.contrib.auth import views as auth_views
from notes.views import cats, tags, notes, profiles, index, registrations
from debug_toolbar.toolbar import debug_toolbar_urls

from django.urls import path


app_name = 'notes'

urlpatterns = [
    path('', index.Home, name='index'),
    path('category-list', cats.CategoryListView.as_view(), name='category-list'),
    path('categories/new/', cats.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', cats.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', cats.CategoryDeleteView.as_view(), name='category-delete'),
]

# notes pattrns
urlpatterns += [
    path('notes/', notes.NoteListView.as_view(), name='note-list'),
    path('notes/new/', notes.NoteCreateView, name='note-create'),
    path('notes/<int:pk>/edit/', notes.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', notes.NoteDeleteView.as_view(), name='note-delete'),
    path('notes/<int:pk>/detail/', notes.NoteDetailView.as_view(), name='note-detail'),
]

# tags patterns 
urlpatterns += [
    path('tags/', tags.TagListView.as_view(), name='tag-list'),
    path('tags/new/', tags.TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/edit/', tags.TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', tags.TagDeleteView.as_view(), name='tag-delete'),
]

# Tags patterns
urlpatterns += [
    path('profiles-list', profiles.ProfileListView.as_view(), name='profile_list'),
    path('profile/<int:pk>/minside', profiles.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/create/', profiles.ProfileCreateView.as_view(), name='profile_create'),
    path('profile/<int:pk>/edit/', profiles.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', profiles.ProfileDeleteView.as_view(), name='profile_delete'),
]

# Authentication URLs
urlpatterns += [
    # Authentication URLs
    # login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # register class view
    path('register/', registrations.RegisterView.as_view(), name='register'),
    path('logout/', registrations.logout_view, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    # ProfileView
    # path('profile/<str:username>', profiles.ProfileView.as_view(), name='profile'),
]

urlpatterns += [
                   # ... the rest of your URLconf goes here ...
               ] + debug_toolbar_urls()
