# Generated by Django 4.1.7 on 2023-03-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_tasktype_task_remove_tasktype_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ManyToManyField(blank=True, related_name='status_tasks', to='webapp.status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='status_tasks', to='webapp.type'),
        ),
    ]
