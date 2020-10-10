from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'project'
urlpatterns = [
    path('project/create/', ProjectCreateView.as_view()),
    path('all/', ProjectsListView.as_view()),
    path('project/detail/<int:pk>/', ProjectDetailView.as_view()),
]
