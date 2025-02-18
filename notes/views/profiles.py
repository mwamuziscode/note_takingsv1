from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from notes.models.profiles import Profile
from notes.views.forms_views import ProfileForm
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User

# List all profiles
class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'notes/profiles/profile_list.html'
    context_object_name = 'profiles'

# class ProfileView(LoginRequiredMixin, View):
#     def get(self, request, username):
#         user = get_object_or_404(User, username=username)
#         return render(request, 'notes/profiles/profile_detail.html', {'user': user})


# View a single profile
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'notes/profiles/profile_detail.html'
    context_object_name = 'profile'

# Create a new profile
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'notes/profiles/profile_form.html'
    success_url = reverse_lazy('profile_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign current user
        return super().form_valid(form)

# Update an existing profile
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'notes/profiles/profile_form.html'
    success_url = reverse_lazy('profile_list')

# Delete a profile
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'notes/profiles/profile_confirm_delete.html'
    success_url = reverse_lazy('profile_list')
