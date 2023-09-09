from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, UpdateView
from apps.accounts.models import CustomUser
from apps.accounts.forms import CustomUserChangeForm
from apps.projects.models import ProjectModel

# Create your views here.
class MyProfileTamplateView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = ProjectModel.objects.all()
        context["total_projects"] = projects
        context["complete_projects"] = projects.filter(status='c')
        context["incomplete_projects"] = projects.exclude(status='c')
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/editProfile.html'
    model = CustomUser
    form_class = CustomUserChangeForm
    context_object_name = 'user'
    success_url = reverse_lazy('profile')

    def get_object(self):
        email = self.kwargs.get('email')
        return self.model.objects.get(email=email)
