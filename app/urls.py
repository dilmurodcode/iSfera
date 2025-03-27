from django.urls import path
from . import views

urlpatterns = [
    path("connections/", views.ConnectionCreateApiView.as_view()),
    path("service-contact/", views.ServiceContactListAPIView.as_view()),
    path("category/<int:pk>/", views.CategorySerializerUpdateView.as_view()),
]