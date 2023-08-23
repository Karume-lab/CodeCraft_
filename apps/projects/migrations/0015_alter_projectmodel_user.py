# Generated by Django 4.2.4 on 2023-08-23 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0014_remove_projectmodel_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmodel",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_projects",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
