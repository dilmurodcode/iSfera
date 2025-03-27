from rest_framework import generics

from . import serializers
from .models import *
from .serializers import ServiceContactSerializer


class ConnectionListAPIViews(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = serializers.ConnectionSerializer


class ConnectionCreateApiView(generics.ListCreateAPIView):

    def get_serializer_class(self):
        print(self.request.method)
        if self.request.method == 'POST':
            return serializers.ModelS
        return serializers.OddiyS

    def get_queryset(self):
        return Connection.objects.all()


class ServiceContactListAPIView(generics.ListCreateAPIView):
    queryset = ServiceContact.objects.all()
    serializer_class = ServiceContactSerializer


class CategorySerializerUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
