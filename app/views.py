from .models import *
from . import serializers
from rest_framework import views
from rest_framework.response import Response


class ConnectionAPIView(views.APIView):

    def get(self, request):
        queryset = Connection.objects.all()
        serializer = serializers.ConnectionSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )



