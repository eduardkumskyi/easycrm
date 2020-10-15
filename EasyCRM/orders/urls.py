from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


app_name = 'order'
urlpatterns = [
    path('order/create/', OrderCreateView.as_view()),
    path('all/', OdersListView.as_view()),
    path('order/detail/<int:pk>/', OderDetailView.as_view()),
    # path('test/', views.tester),
]
