from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user',)
        model = Entry


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'password')
        model = User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'email')
        model = User

