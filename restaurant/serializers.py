#define Serializer class for User model
from django.contrib.auth.models import User
from .models import Booking, MenuItem
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']