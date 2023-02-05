# Generated by Django 3.2 on 2023-02-05 04:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_tempcourses'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TempCourses',
        ),
        migrations.AlterModelOptions(
            name='courseteachers',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('course', 'num'), 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created',), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='courseteachers',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseteachers',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Edited'),
        ),
    ]