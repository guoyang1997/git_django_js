
from django.contrib import admin
from django.urls import path
from jishi import views
urlpatterns = [
    path('dev2/', views.dev2),
]
