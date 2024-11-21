# from django.contrib import admin
from django.urls import path
import views

app_name = "article"

urlpatterns = [
    path('create/', views.index, name="index")
]
