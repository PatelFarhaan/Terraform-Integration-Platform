from django.urls import path
from aws import views


app_name = 'aws'
urlpatterns = [
    path('index', views.index, name="index"),
    path('dashboard/', views.dashboardform, name="dashboard"),
    path('createapp/', views.createapp, name="createapp"),
    path('manageapp/', views.manageapp, name="manageapp"),
]