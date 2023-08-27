from django.shortcuts import render
from typing import Any, Dict
from django.db.models import Q
from django.views.generic import TemplateView
from apps.projects.models import ProjectModel, TaskModel
# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

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
