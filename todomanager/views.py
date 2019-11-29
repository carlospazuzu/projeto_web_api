from .models import ProjectUser, Project, Label, Activity 
from .serializers import ProjectUserSerializer, ProjectSerializer, LabelSerializer, ActivitySerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions, filters
from .permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters


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

    def filter_queryset(self, queryset):
        pass


class LabelDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    name = 'label-detail'


class ProjectList(generics.ListCreateAPIView): 
    # permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project-list'

    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name']

    # filter_fields = ['name']
    # search_fields = ['name']
    # ordering_fields = ['name']

    # def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project-detail'



class ActivityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    name = 'activity-list'

    def filter_queryset(self, queryset):
        pass



class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    name = 'activity-detail'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
