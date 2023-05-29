from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index.html", views.index, name="index"),
    path("about.html", views.about, name="about"),
]
