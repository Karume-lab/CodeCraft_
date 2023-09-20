from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ProjectModel(models.Model):
    user = models.ForeignKey('accounts.CustomUser', verbose_name='User', on_delete=models.CASCADE, related_name='user_projects', blank=True, null=True)
    title = models.CharField(max_length=45, unique=True)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Date Due')
    date_updated = models.DateField(auto_now=True, auto_now_add=False)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    description = models.TextField(blank=True, null=True)
    WORKING_ON = 'w'
    PENDING = 'p'
    COMPLETED = 'c'
    DRAFT = 'd'
    STATUS_CHOICES = [
        (WORKING_ON, 'Working on'),
		(PENDING, 'Pending'),
		(COMPLETED, 'Completed'),
		(DRAFT, 'Draft'),
	]
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=PENDING)
    HIGH = '1'
    MEDIUM = '2'
    LOW = '3'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=1, default=MEDIUM, null=True)
    image = models.ImageField(upload_to='projects/', height_field=None, width_field=None, null=True, blank=True)
    slug = models.SlugField(db_index=True)

    def update_progress(self):
        total_tasks = self.tasks.count()
        completed_tasks = self.tasks.filter(status=TaskModel.COMPLETED).count()
        if total_tasks > 0:
            self.progress = int((completed_tasks / total_tasks) * 100)
        else:
            self.progress = 0
        self.save()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def get_absolute_url(self):
        return reverse(
                    'projects:detail',
                    args=[
                        self.slug,
                        self.date_created.year,
                        self.date_created.month,
                        self.date_created.day
                    ]
                )
    

    def __str__(self):
        return self.title

class TaskModel(models.Model):
    project = models.ForeignKey('projects.ProjectModel', on_delete=models.CASCADE, related_name='tasks', verbose_name='Project')
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Date Due')
    date_updated = models.DateField(auto_now=True, auto_now_add=False)
    description = models.TextField(blank=True, null=True)
    PENDING = 'p'
    COMPLETED = 'c'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=PENDING)
    slug = models.SlugField(db_index=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


    def __str__(self):
        return f'{self.project.title} - {self.description}'

class SubTaskModel(models.Model):
    task = models.ForeignKey('projects.TaskModel', on_delete=models.CASCADE, related_name='subtasks', verbose_name='Task')
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Date Due')
    date_updated = models.DateField(auto_now=True, auto_now_add=False)
    description = models.TextField(blank=True, null=True)
    PENDING = 'p'
    COMPLETED = 'c'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=PENDING)
    slug = models.SlugField(db_index=True)

    class Meta:
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'

    def __str__(self):
        return f'{self.task.project.title} - {self.description}'
