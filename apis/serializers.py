from rest_framework import serializers
from todos import models
from django.contrib.auth.models import User


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
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'project',
            'desc',
            'is_completed',
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
