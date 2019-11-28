from .models import ProjectUser, Project, Label, Activity 
from .serializers import ProjectUserSerializer, ProjectSerializer, LabelSerializer, ActivitySerializer
from rest_framework import generics


class ProjectUserList(generics.ListCreateAPIView): 
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    name = 'projectuser-list'


class ProjectUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    name = 'projectuser-detail'


class LabelList(generics.ListCreateAPIView): 
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    name = 'label-list'


class LabelDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    name = 'label-detail'


class ProjectList(generics.ListCreateAPIView): 
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project-list'


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project-detail'


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    name = 'activity-list'


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    name = 'activity-detail'

