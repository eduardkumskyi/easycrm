from rest_framework import generics
from .serializers import OrderDetailSerializer, OrdersListSerializer,\
    ProjectsListSerializer, ProjectDetailSerializer
from .models import Order, Project
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated, )


class OdersListView(generics.ListAPIView):
    serializer_class = OrdersListSerializer
    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
    permission_classes = ()


class OderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.id)
    permission_classes = (IsOwnerOrReadOnly, )


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
