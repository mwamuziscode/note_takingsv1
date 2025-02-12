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
from . import views
handler404 = 'notes.views.custom_404_view'


from django.urls import path

#vimport CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from . import views 

urlpatterns = [
    path('', views.index, name='index'),    
    path('category-list', views.CategoryListView.as_view(), name='category-list'),
    path('categories/new/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]

# notes pattrns
urlpatterns += [
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/new/', views.CategoryCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDetailView.as_view(), name='note-delete'),
]

# tags patterns 
urlpatterns += [
    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/new/', views.TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
]


# Tags patterns
urlpatterns += [
    path('tags/', views.TagListView.as_view(), name='tags-list'),
    path('tags/new/', views.TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
]




# Authentication URLs
urlpatterns += [
    # Authentication URLs

    #login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #register class view
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    #ath('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    #ath('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    #ath('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    #ath('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    #ath('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

]