from rest_framework import serializers
from .models import ProjectUser, Label, Project, Activity  


class ProjectUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectUser
        fields = ['url', 'id', 'name']


class LabelSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Label
        fields = ['url', 'id', 'name']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    activities = serializers.SlugRelatedField(many=True, queryset=Activity.objects.all(), slug_field='name')

    class Meta:
        model = Project
        fields = ['url', 'id', 'name', 'priority', 'owner', 'contributors', 'label', 'activities']    


class ActivitySerializer(serializers.HyperlinkedModelSerializer): 
    project = serializers.SlugRelatedField(many=False, queryset=Project.objects.all(), slug_field='name')

    class Meta:
        model = Activity
        fields = ['url', 'id', 'name', 'was_concluded', 'date_created', 'date_concluded', 'concluded_by', 'project']    