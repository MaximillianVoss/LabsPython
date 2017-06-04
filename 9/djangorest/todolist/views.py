from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound

from .serializers import TaskSerializer, TasklistSerializer, TagSerializer, UserSerializer
from .models import Task, Tasklist, Tag, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagTypeViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TasklistCreateView(generics.ListCreateAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer


class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer


class TaskCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        list_id = self.kwargs.get('list_id', None)
        if list_id is not None:
            queryset = queryset.filter(tasklist_id=list_id)
        return queryset

    def perform_create(self, serializer):
        list_id = self.kwargs.get('list_id', None)
        try:
            tasklist = Tasklist.objects.get(pk=list_id)
        except Tasklist.DoesNotExist:
            raise NotFound()
        serializer.save(tasklist=tasklist)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        list_id = self.kwargs.get('list_id', None)
        if list_id is not None:
            queryset = queryset.filter(tasklist_id=list_id)
        return queryset
