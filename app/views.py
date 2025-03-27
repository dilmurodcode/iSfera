from django.shortcuts import render
from .models import *
from rest_framework import views, generics
from . import serializers
from rest_framework.response import Response

class ConnectionListAPIViews(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = serializers.ConnectionSerializer
