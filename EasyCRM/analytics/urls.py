from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


app_name = 'analytics'


urlpatterns = [
    path('analytics/', views.index, name='product_detail'),
]
