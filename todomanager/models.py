from django.db import models

class ProjectUser(models.Model):
    name = models.CharField(max_length=254, null=False, unique=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


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
    # owner = models.ForeignKey(ProjectUser, related_name='proprietario', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='projects', null=True, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('auth.User', blank=True)
    label = models.ForeignKey(Label, related_name='etiqueta', on_delete=models.CASCADE)
    # activities = models.ForeignKey('Activity', null=True, related_name='atividades', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=254, null=False)
    was_concluded = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_concluded = models.DateTimeField(null=True)
    concluded_by = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='atividades', on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Timeline(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    log = models.CharField(max_length=254)


    def __str__(self):
        return str(self.timestamp.strftime("%b %d %Y %H:%M:%S")) + ' - ' + self.log