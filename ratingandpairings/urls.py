from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="LoginPage"),
    path("home/", views.HomeView.as_view(), name="HomePage"),
]
