# Generated by Django 3.1.7 on 2021-05-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]