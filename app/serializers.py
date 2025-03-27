from .models import *
from rest_framework import serializers

class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = (
            'id', 'title', 'image', 'description', 'order'
        )