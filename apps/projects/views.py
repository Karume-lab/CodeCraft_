from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import ProjectModel
from .forms import ProjectForm, TaskForm, SubTaskForm

# Create your views here.
class ProjectCreateView(CreateView):
    template_name = 'projects/create.html'
    model = ProjectModel
    form_class = ProjectForm

    def post(self, request):
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.slug = slugify(form.cleaned_data.get('description'))
            new_project.save()
        return redirect(reverse('projects:list'))

class ProjectUpdateView(UpdateView):
    template_name = 'projects/edit.html'
    model = ProjectModel
    form_class = ProjectForm
    success_url = reverse_lazy('projects:list')

class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete.html'
    model = ProjectModel
    context_object_name = 'project'

    def get_success_url(self):
        return reverse_lazy('projects:list')

class ProjectsListView(ListView):
    template_name = 'projects/list.html'
    model = ProjectModel
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    queryset = ProjectModel.objects.all()
    context_object_name = 'project'

    def get_project(self):
        return get_object_or_404(
            ProjectModel,
            slug=self.kwargs.get('slug'),
            date_created__year=self.kwargs.get('year'),
            date_created__month=self.kwargs.get('month'),
            date_created__day=self.kwargs.get('day')
        )
