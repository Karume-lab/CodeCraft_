from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import ProjectModel, TaskModel, SubTaskModel
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
            return redirect(
                        reverse(
                            'projects:detail',
                            args=[
                                    new_project.slug,
                                    new_project.date_created.year,
                                    new_project.date_created.month,
                                    new_project.date_created.day
                                ]
                        )
                    )

class ProjectUpdateView(UpdateView):
    template_name = 'projects/edit.html'
    model = ProjectModel
    form_class = ProjectForm
    success_url = reverse_lazy('projects:list')

class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete.html'
    model = ProjectModel
    context_object_name = 'project'
    success_url = reverse_lazy('projects:list')

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

class TaskCreateView(CreateView):
    template_name = 'projects/tasks/create.html'
    model = TaskModel
    form_class = TaskForm

class TaskCreateView(CreateView):
    template_name = 'projects/tasks/create_task.html'
    model = TaskModel
    form_class = TaskForm

    def post(self, request, slug, year, month, day):
        form = TaskForm(data=request.POST)
        project = get_object_or_404(
            ProjectModel,
            slug=slug,
            date_created__year=year,
            date_created__month=month,
            date_created__day=day
        )
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.project = project
            new_task.slug = slugify(form.cleaned_data.get('description'))
            new_task.save()
            return redirect(
                        reverse(
                            'projects:detail',
                            args=[
                                project.slug,
                                project.date_created.year,
                                project.date_created.month,
                                project.date_created.day
                            ]
                        )
                    )

class TaskUpdateView(UpdateView):
    template_name = 'projects/tasks/edit.html'
    model = TaskModel
    form_class = TaskForm
    success_url = reverse_lazy('projects:list')

class TaskDeleteView(DeleteView):
    template_name = 'projects/tasks/delete.html'
    model = TaskModel
    context_object_name = 'task'
    success_url = reverse_lazy('projects:list')
