from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("parse-act", views.parse_act, name="parse-act"),
]