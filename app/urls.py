from django.urls import path
from . import views

urlpatterns = [
    path("connections-list/", views.ConnectionListAPIViews.as_view())
]