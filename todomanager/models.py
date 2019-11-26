from django.db import models

class ProjectUser(models.Model):
    name = models.CharField(max_length=254, null=False)


class Label(models.Model):
    name = models.CharField(max_length=50, null=False)


class Project(models.Model):

    NORMAL = 'N'
    MEDIUM = 'M'
    HIGH = 'H'
    CRITICAL = 'C'

    PRIORITY_CHOICES = [
        (NORMAL, 'Normal'),
        (MEDIUM, 'Moderada'),
        (HIGH, 'Alta'),
        (CRITICAL, 'Crítica'),
    ]

    name = models.CharField(max_length=200, null=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=NORMAL)
    owner = models.ForeignKey(ProjectUser, related_name='projeto', on_delete=models.CASCADE)
    contributors = models.ManyToManyField(ProjectUser)
    label = models.ForeignKey(Label, related_name='etiqueta', on_delete=models.CASCADE)


class Activity(models.Model):
    name = models.CharField(max_length=254, null=False)
    was_concluded = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_concluded = models.DateTimeField()
    concluded_by = models.OneToOneField(ProjectUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='projeto', on_delete=models.CASCADE)



    
