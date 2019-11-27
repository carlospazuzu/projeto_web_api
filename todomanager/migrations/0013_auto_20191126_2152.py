# Generated by Django 2.2.7 on 2019-11-27 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todomanager', '0012_project_activities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='activities',
        ),
        migrations.AddField(
            model_name='project',
            name='activities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='todomanager.Activity'),
        ),
    ]
