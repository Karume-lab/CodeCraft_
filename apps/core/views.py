from typing import Any, Dict, Optional
import random
from datetime import datetime
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from apps.projects.models import ProjectModel, TaskModel
# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'

class HomeTemplateView(ListView):
    template_name = 'core/home.html'
    model = ProjectModel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = ProjectModel.objects.all()
        context['today_projects'] = ProjectModel.objects.filter(date_due=datetime.today().date())
        return context

class SearchTemplateView(TemplateView):
    template_name = 'core/search_results.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        search_query = self.request.GET.get('search_query')
        context = super().get_context_data(**kwargs)
        context['project_results'] = ProjectModel.objects.filter(
                                                                Q(title__icontains=search_query) |
                                                                Q(description__icontains=search_query)
                                                            )
        context['task_results'] = TaskModel.objects.filter(description__icontains=search_query)
        return context

class ShareTemplateView(TemplateView):
    template_name = 'core/share.html'

class FeedbackTemplateView(TemplateView):
    template_name = 'core/feedback.html'

class RandomizeDetailView(DetailView):
    template_name = 'core/randomize.html'
    model = ProjectModel
    context_object_name = 'project'

    def get_object(self):
        random_project = random.choice(ProjectModel.objects.all())
        return random_project
