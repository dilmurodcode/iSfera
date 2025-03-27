from rest_framework import generics

from . import serializers
from .models import *


class ConnectionListAPIViews(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = serializers.ConnectionSerializer
