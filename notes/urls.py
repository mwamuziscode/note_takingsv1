"""
URL configuration for notetaking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from notes.views import cats, tags, notes, views, profiles, index, registrations



from django.urls import path


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
    path('notes/new/', notes.NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/edit/', notes.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', notes.NoteDetailView.as_view(), name='note-delete'),
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
    path('profile/<int:pk>', profiles.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/create/', profiles.ProfileCreateView.as_view(), name='profile_create'),
    path('profile/<int:pk>/edit/', profiles.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', profiles.ProfileDeleteView.as_view(), name='profile_delete'),
]



# Authentication URLs
urlpatterns += [
    # Authentication URLs

    #login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #register class view
    path('register/', registrations.RegisterView.as_view(), name='register'),
    path('logout/', registrations.logout_view, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    # ProfileView
    # path('profile/<str:username>', profiles.ProfileView.as_view(), name='profile'),
]