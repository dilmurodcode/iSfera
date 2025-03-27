from .models import *
from . import serializers
from rest_framework import views
from rest_framework.response import Response


class InfoAPIView(views.APIView):

    def get(self, request):
        queryset = Info.objects.all()
        serializer = serializers.InfoSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )



