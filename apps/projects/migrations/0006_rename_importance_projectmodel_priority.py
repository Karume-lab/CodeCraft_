# Generated by Django 4.2.4 on 2023-09-07 10:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0005_alter_projectmodel_importance"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectmodel",
            old_name="importance",
            new_name="priority",
        ),
    ]