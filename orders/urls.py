# urls that the user can visit. This file maps those to views.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
