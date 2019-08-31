# urls that the user can visit. This file maps those to views.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # make available access to individual pizza by introducing id variable
    path("<int:pizza_id>", views.pizza, name="pizza"),
]
