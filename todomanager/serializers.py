from rest_framework import serializers
from .models import Label, Project, Activity, Timeline  
from django.contrib.auth.models import User

"""
class ProjectUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectUser
        fields = ['url', 'id', 'name']
"""

class LabelSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Label
        fields = ['url', 'id', 'name']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # activities = serializers.SlugRelatedField(many=True, queryset=Activity.objects.all(), slug_field='name')
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['url', 'id', 'name', 'priority', 'owner', 'contributors', 'label', 'atividades'] 


class ActivitySerializer(serializers.HyperlinkedModelSerializer): 
    # project = serializers.SlugRelatedField(many=False, queryset=Project.objects.all(), slug_field='name')

    class Meta:
        model = Activity
        fields = ['url', 'id', 'name', 'was_concluded', 'date_created', 'date_concluded', 'concluded_by', 'project']    


class UserSerializer(serializers.ModelSerializer):
    # projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id', 'timestamp', 'log']
