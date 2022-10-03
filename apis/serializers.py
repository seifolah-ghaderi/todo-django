from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework import serializers
from todos import models
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'desc',
        )
        model = models.Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'first_name',
            'last_name',
        )
        model = User
class UserIDSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id'
        )
        model = User
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'project',
            'desc',
            'is_completed',
        )
        model = models.Task

class TaskUpdateSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True, many=True)
    class Meta:
        fields = (
            'id',
            'assignee',
        )
        model = models.Task

class UserTasksSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True, many=True)
    class Meta:
        fields = (
            'id',
            'title',
            'desc',
            'assignee',
        )
        model = models.Task


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'desc',
        )
        model = models.Project


class TaskUpdateSerializer(serializers.ModelSerializer):
   
    #asignee=UserSerializer(read_only=True, many=True)
    assing_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='asignee')

   
    class Meta:
        fields = (
            'id',
            'assing_ids',
        )
        model = models.Task
    
    def update(self, instance, validated_data):
        validated_data['assing_ids'] = filter(None, validated_data['assing_ids'])
        for id in validated_data['assing_ids']:
            skill = User.objects.get(pk=id)
            instance.asignee.add(skill)

        return instance



