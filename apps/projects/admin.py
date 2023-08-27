from django.contrib import admin
from .models import ProjectModel, TaskModel, SubTaskModel
# Register your models here.

@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = [
		'title',
        'user',
		'date_created',
		'date_due',
		'description',
		'status',
		'image',
	]

    prepopulated_fields = {
        'slug': ('title',)
	}

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = [
        'project',
		'date_created',
		'date_due',
		'description',
		'status',
		'slug',
	]

    prepopulated_fields = {
        'slug': ('description',)
	}


@admin.register(SubTaskModel)
class SubTaskModelAdmin(admin.ModelAdmin):
    list_display = [
        'task',
		'date_created',
		'date_due',
		'description',
		'status',
		'slug',
	]

    prepopulated_fields = {
        'slug': ('description',)
	}
