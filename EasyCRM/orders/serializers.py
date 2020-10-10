from rest_framework import serializers
from .models import Order
from .forms import UserFilteredPrimaryKeyRelatedField
from projects.models import Project


class OrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'second_name', 'middle_name', 'waybill', 'state')


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'
        project = UserFilteredPrimaryKeyRelatedField(queryset=Project.objects.all)
