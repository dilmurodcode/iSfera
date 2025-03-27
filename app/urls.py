from django.urls import path
from . import views

urlpatterns = [
    path('connection-list/', views.ConnectionAPIView.as_view())
]