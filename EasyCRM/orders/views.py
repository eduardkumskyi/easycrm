from django.shortcuts import render
from rest_framework import generics

from django.http import HttpResponse
# from apiconnections.tasks import periodic_np_status_update
from .serializers import OrderDetailSerializer, OrdersListSerializer
from .models import Order
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# from .tasks import periodic_np_status_update_all


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

# def tester(request):
#     periodic_np_status_update_all.delay()
#     return HttpResponse("Пошло")
