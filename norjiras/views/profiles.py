from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from notes.models.profiles import Profile
from notes.views.forms_views import ProfileForm
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

# Ensure only logged-in users can access their own profile
from django.shortcuts import redirect


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "notes/profiles/profile_detail.html"

    def get_object(self):
        """Redirect user to profile creation if they don't have a profile."""
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        if created:
            return redirect("profile_create")  # Redirect to profile creation view
        return profile


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "notes/profiles/profile_form.html"

    def get_object(self):
        """Ensure user can only update their own profile."""
        return get_object_or_404(Profile, user=self.request.user)

    def test_func(self):
        """Check if the logged-in user is the owner of the profile."""
        profile = self.get_object()
        return self.request.user == profile.user

    def get_success_url(self):
        url = reverse("profile_list")
        print(f"MR KING DEBUGGER: Redirecting to {url}")
        return url


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = "notes/profiles/profile_confirm_delete.html"
    success_url = reverse_lazy("profile_list")

    def get_object(self):
        """Ensure user can only delete their own profile."""
        return get_object_or_404(Profile, user=self.request.user)

    def test_func(self):
        """Check if the logged-in user is the owner of the profile."""
        profile = self.get_object()
        return self.request.user == profile.user


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "notes/profiles/profile_form.html"
    success_url = reverse_lazy("profile_list")

    def form_valid(self, form):
        """Ensure the logged-in user is automatically set as the profile owner."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "notes/profiles/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        """Return only the logged-in user's profile."""
        return Profile.objects.filter(user=self.request.user)
