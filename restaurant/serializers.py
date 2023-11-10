#define Serializer class for User model
from django.contrib.auth.models import User
from .models import Booking, Menu
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookingSerializer(serializers.ModelSerializer):
    model = Booking
    fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    model = Menu
    fields = '__all__'