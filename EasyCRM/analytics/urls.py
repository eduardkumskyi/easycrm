from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


app_name = 'analytics'


urlpatterns = [
    path('analytics/orders', views.orders),
    path('analytics/money', views.money),
]
