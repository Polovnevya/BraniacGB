# Generated by Django 3.2 on 2023-01-28 18:17

from django.db import migrations
from django.shortcuts import get_object_or_404


def forwards_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model("mainapp", "Lesson")
    Courses = apps.get_model("mainapp", "Courses")
    
    # Create model's objects
    Lesson.objects.create(
        course = get_object_or_404(Courses, pk=1),
        num = 1,
        title ="Lesson 1 from data_migrations",
        description = "Описание урока",
        description_as_markdown = False,
    )


def reverse_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model("mainapp", "Lesson")
    # Delete objects
    Lesson.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_courses_data_migration'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]