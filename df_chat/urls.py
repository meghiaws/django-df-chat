# chat/urls.py
from . import views
from django.urls import path


# test

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
