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
    owner = ProjectUserSerializer(many=False, read_only=True)
    contributors = ProjectUserSerializer(many=True, read_only=True)
    label = serializers.PrimaryKeyRelatedField(many=False, queryset=Label.objects.all())  

    class Meta:
        model = Project
        fields = ['url', 'id', 'priority', 'owner', 'contributors', 'label']    


class ActivitySerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Activity
        fields = ['url', 'id', 'name', 'was_concluded', 'date_created', 'date_concluded', 'concluded_by', 'project']    




