# Generated by Django 4.2.4 on 2023-08-28 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=45)),
                ("date_created", models.DateField(auto_now_add=True)),
                (
                    "date_due",
                    models.DateField(blank=True, null=True, verbose_name="Date Due"),
                ),
                ("date_updated", models.DateField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("w", "Working on"),
                            ("p", "Pending"),
                            ("c", "Completed"),
                            ("d", "Draft"),
                        ],
                        default="p",
                        max_length=1,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="projects/"),
                ),
                ("slug", models.SlugField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_projects",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
            },
        ),
        migrations.CreateModel(
            name="TaskModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateField(auto_now_add=True)),
                (
                    "date_due",
                    models.DateField(blank=True, null=True, verbose_name="Date Due"),
                ),
                ("date_updated", models.DateField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("p", "Pending"), ("c", "Completed")],
                        default="p",
                        max_length=1,
                    ),
                ),
                ("slug", models.SlugField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="projects.projectmodel",
                        verbose_name="Project",
                    ),
                ),
            ],
            options={
                "verbose_name": "Task",
                "verbose_name_plural": "Tasks",
            },
        ),
        migrations.CreateModel(
            name="SubTaskModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateField(auto_now_add=True)),
                (
                    "date_due",
                    models.DateField(blank=True, null=True, verbose_name="Date Due"),
                ),
                ("date_updated", models.DateField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("p", "Pending"), ("c", "Completed")],
                        default="p",
                        max_length=1,
                    ),
                ),
                ("slug", models.SlugField()),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subtasks",
                        to="projects.taskmodel",
                        verbose_name="Task",
                    ),
                ),
            ],
            options={
                "verbose_name": "SubTask",
                "verbose_name_plural": "SubTasks",
            },
        ),
    ]
