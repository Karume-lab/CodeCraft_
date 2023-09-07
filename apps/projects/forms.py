from django import forms
from .models import  ProjectModel, TaskModel, SubTaskModel

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = [
            'title',
            'date_due',
            'description',
            'importance',
            'image',
		]

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'description',
            'date_due',
		]

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTaskModel
        fields = [
            'description',
            'date_due',
		]
