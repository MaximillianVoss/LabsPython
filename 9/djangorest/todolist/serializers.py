from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Task, Tasklist, Tag, User


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)

    # status = serializers.ChoiceField(choices=STATUSES, default='New')
    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lname')
        ordering = 'name'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
        ordering = 'name'


class TagSerializer2(PrimaryKeyRelatedField, serializers.ModelSerializer, ):
    class Meta:
        model = Tag
        fields = ('name',)
        ordering = 'name'


class Meta:
    model = Tasklist
    fields = ('name', 'owner')


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer2(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'description', 'tags', 'completed',
            'date_created', 'date_modified', 'due_date', 'priority'
        )
        read_only_fields = ('date_created', 'date_modified')


class TaskSerializer2(PrimaryKeyRelatedField, serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)


class TasklistSerializer2(PrimaryKeyRelatedField, serializers.ModelSerializer):
    tasks = TaskSerializer2(many=True, queryset=Task.objects.all())


class TasklistSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer2(many=True, queryset=Task.objects.all())

    class Meta:
        model = Tasklist
        fields = ('name', 'owner', 'tasks')
