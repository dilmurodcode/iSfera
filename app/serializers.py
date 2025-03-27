from .models import *
from rest_framework import serializers


class ModelS(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class OddiyS(serializers.Serializer):
    full_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('full_name', 'phone', 'email')


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', "price")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'order')


class ServiceContactSerializer(serializers.ModelSerializer):
    connection = ConnectionSerializer()
    service = serviceSerializer()
    category = CategorySerializer()

    class Meta:
        model = ServiceContact
        fields = ('connection', 'service', 'category')

    def create(self, validated_data):
        connection = validated_data.get('connection')
        service = validated_data.get('service')
        category = validated_data.get('category')

        # service = Service.objects.create(**service)

        service = Service.objects.create(
            name=service.get('name'),
            price=1000,
        )

        connection = Connection.objects.create(**connection)
        category = Category.objects.create(**category)

        return ServiceContact.objects.create(connection=connection, service=service, category=category)





