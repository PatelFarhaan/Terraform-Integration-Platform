from aws import views
from django.urls import path


app_name = 'aws'
urlpatterns = [
    path('index', views.index, name="index"),
    path('dashboard/', views.dashboardform, name="dashboard"),
    path('createapp/', views.createapp, name="createapp"),
    path('manageapp/', views.manageapp, name="manageapp"),
    path('createenv/', views.infraCompute, name="createenv"),
    path('manageenv', views.manageenv, name="manageenv"),
    path('infradb/', views.infradatabase, name="infradb"),
    path('infracicd/', views.infracicd, name="infracicd"),
    path('createmigrations/', views.createmigrations, name="createmigrations"),
    path('managemigrations/', views.managemigrations, name="managemigrations"),

]