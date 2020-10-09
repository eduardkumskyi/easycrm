from rest_framework import serializers
from .models import Order, Project
from .forms import UserFilteredPrimaryKeyRelatedField


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


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'country', 'np_api', 'user')


class ProjectDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = '__all__'
