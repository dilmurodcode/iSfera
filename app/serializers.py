from .models import *
from rest_framework import serializers

class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection
        fields = (
            'id', 'full_name', 'phone', 'email'
        )


