from .models import Project, Label, Activity, Timeline
from .serializers import ProjectSerializer, LabelSerializer, ActivitySerializer, UserSerializer, TimelineSerializer, TokenObtainPairSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions, filters as rfilters
from .permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from rest_framework_simplejwt.views import TokenObtainPairView

"""
class ProjectUserList(generics.ListCreateAPIView): 
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    name = 'projectuser-list'


class ProjectUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    name = 'projectuser-detail'
"""

class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class LabelList(generics.ListCreateAPIView): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    name = 'label-list'

    # def filter_queryset(self, queryset):
    #     pass

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        # print(self.request.data)
        Timeline.objects.create(log="A Etiqueta " + self.request.data['name'] + " foi criada!")
        serializer.save()


class LabelDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    name = 'label-detail'


class ProjectList(generics.ListCreateAPIView): 
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project-list'

    filter_backends = [filters.DjangoFilterBackend, rfilters.SearchFilter, rfilters.OrderingFilter]
    filterset_fields = ['label']
    search_fields = ['name']
    ordering_fields = ['name']

    # filter_fields = ['name']
    # search_fields = ['name']
    # ordering_fields = ['name']

    def perform_create(self, serializer):
        Timeline.objects.create(log="O usuário " + str(self.request.user) + " criou o Projeto " + self.request.data['name'] + "!")        
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project-detail'



class ActivityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    name = 'activity-list'

    filter_backends = [filters.DjangoFilterBackend, rfilters.SearchFilter, rfilters.OrderingFilter]
    filterset_fields = ['project', 'date_created']
    search_fields = ['name']
    ordering_fields = ['name']

    # def filter_queryset(self, queryset):
    #     pass



class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    name = 'activity-detail'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class TimelineList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    name = 'timeline-list'

