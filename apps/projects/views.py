from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.utils.text import slugify
from datetime import date
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, View
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
    context_object_name = 'project'
    success_url = reverse_lazy('projects:list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.slug = slugify(form.cleaned_data.get('title'))
            new_project.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete.html'
    model = ProjectModel
    context_object_name = 'project'
    success_url = reverse_lazy('projects:list')

class ProjectsListView(ListView):
    template_name = 'projects/list.html'
    queryset = ProjectModel.objects.all()
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_by = self.request.GET.get('filter_by')

        if filter_by == 'today':
            queryset = queryset.filter(date_due__day=date.today().day)
        elif filter_by == 'this_week':
            queryset = queryset.filter(date_due__week=date.today().isocalendar()[1])
        elif filter_by == 'my_month':
            queryset = queryset.filter(date_due__month=date.today().month)

        return queryset.filter(user=self.request.user)

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
    template_name = 'projects/tasks/create.html'
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
            project.update_progress()
            project.save()
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.slug = slugify(form.cleaned_data.get('description'))
            new_task.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        project = self.object.project
        return project.get_absolute_url()

class TaskDeleteView(DeleteView):
    template_name = 'projects/tasks/delete.html'
    model = TaskModel
    context_object_name = 'task'

    def get_success_url(self):
        project = self.object.project
        project.update_progress()
        project.save()
        return project.get_absolute_url()


class MarkTaskCompleteView(View):
    def post(self, request, slug, year, month, day):
        task = get_object_or_404(TaskModel, slug=slug, date_created__year=year, date_created__month=month, date_created__day=day)
        if task.status == TaskModel.COMPLETED:
            task.status = TaskModel.PENDING
        else:
            task.status = TaskModel.COMPLETED
        task.save()
        project = task.project
        project.update_progress()
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
