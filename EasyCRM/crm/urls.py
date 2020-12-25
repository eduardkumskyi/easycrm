from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


app_name = 'crm'
urlpatterns = [
    path('projects/create/', ProjectCreateView.as_view()),
    path('projects/all/', ProjectsListView.as_view()),
    path('projects/detail/<int:pk>/', ProjectDetailView.as_view()),

    path('orders/create/', OrderCreateView.as_view()),
    path('orders/all/', OdersListView.as_view()),
    path('orders/detail/<int:pk>/', OderDetailView.as_view()),
]
