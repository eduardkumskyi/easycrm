from django.shortcuts import render
from rest_framework import generics

from orders.permissions import IsOwnerOrReadOnly
from .serializers import ProjectsListSerializer, ProjectDetailSerializer
from .models import Project
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectDetailSerializer
    permission_classes = (IsAuthenticated, )


class ProjectsListView(generics.ListAPIView):
    serializer_class = ProjectsListSerializer
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user=user)
    permission_classes = ()


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user.id)
    permission_classes = (IsOwnerOrReadOnly, )
