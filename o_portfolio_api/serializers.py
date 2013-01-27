from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user',)
        model = Entry


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'password')
        model = User

    def restore_object(self, attrs, instance=None):
        user = User(
            first_name = attrs['first_name'],
            last_name = attrs['last_name'],
            username = attrs['username'],
        )
        user.set_password(attrs['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'email')
        model = User

