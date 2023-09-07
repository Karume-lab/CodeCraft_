from typing import Any, Dict, Optional
import random
from datetime import date
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.projects.models import ProjectModel, TaskModel

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'

class HomeListView(LoginRequiredMixin, ListView):
    model = ProjectModel
    template_name = 'core/home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        sort = self.request.GET.get('sort_by')
        queryset = super().get_queryset().filter(user=self.request.user)

        if sort == 'a-z':
            queryset = queryset.order_by('title')
        elif sort == 'date':
            queryset = queryset.order_by('date_created')
        elif sort == 'progress':
            queryset = queryset.order_by('-progress')
        elif sort == 'priority':
            queryset = queryset.order_by('priority')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today_projects'] = ProjectModel.objects.filter(date_due=date.today(), user=self.request.user)
        return context

class SearchTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/search_results.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        search_query = self.request.GET.get('search_query')
        context = super().get_context_data(**kwargs)
        context['project_results'] = ProjectModel.objects.filter(
                                                                Q(title__icontains=search_query) |
                                                                Q(description__icontains=search_query),
                                                                user=self.request.user
                                                            )
        context['task_results'] = TaskModel.objects.filter(description__icontains=search_query, user=self.request.user)
        return context

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        name = data.get("name")
        email = data.get("email")
        subject = data.get("subject")
        description = data.get("description")
        settings.DEFAULT_FROM_EMAIL = email

        # Compose the email body
        body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nDescription: {description}"

        # Send the email
        send_mail(subject, body, email, ["ephraimshikanga@gmail.com"])

        return JsonResponse({"message": "Email sent successfully"})
    
    return JsonResponse({"error": "Invalid request method"})

class FeedbackTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/feedback.html'

class RandomizeDetailView(DetailView):
    template_name = 'core/randomize.html'
    model = ProjectModel
    context_object_name = 'project'

    def get_object(self):
        random_project = random.choice(ProjectModel.objects.filter(user=self.request.user))
        return random_project

class ImportantProjectsListView(LoginRequiredMixin, ListView):
    template_name = 'projects/list.html'
    queryset = ProjectModel.objects.all()
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(priority='1', user=self.request.user)

class MissedDealineProjectsListView(LoginRequiredMixin, ListView):
    model = ProjectModel
    template_name = 'core/deadline.html'
    context_object_name = 'deadline_projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(date_due__lt=date.today(), user=self.request.user)
