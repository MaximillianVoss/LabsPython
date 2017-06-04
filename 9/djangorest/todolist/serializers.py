from rest_framework import serializers
from .models import Task, Tasklist, Tag, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lname')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'name', 'description', 'tags', 'completed',
            'date_created', 'date_modified', 'due_date', 'priority'
        )
        read_only_fields = ('date_created', 'date_modified')


class TasklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tasklist
        fields = ('name','owner', 'tasks')
