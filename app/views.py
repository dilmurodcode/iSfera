from django.shortcuts import render
from .models import *
from rest_framework import views
from . import serializers
from rest_framework.response import Response

class ConnectionListAPIViews(views.APIView):

    def get(self, request):
        data = Connection.objects.filter()
        serializer = serializers.ConnectionSerializer(data, many=True)
        return Response(
            data=serializer.data,)
