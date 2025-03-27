from django.urls import path
from . import views

urlpatterns = [
    path("connections/", views.ConnectionListAPIViews.as_view())
]