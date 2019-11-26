from rest_framework import serializers
from projeto_web_api.models import ProjectUser, Label


class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = ['name']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']