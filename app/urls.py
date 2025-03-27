from django.urls import path
from . import views

urlpatterns = [
    path('info-list/', views.InfoAPIView.as_view())
]