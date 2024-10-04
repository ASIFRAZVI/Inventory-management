from rest_framework import serializers
from apps.authentication.models.user_auth import CustomUser


class auth_serializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)


class login_serializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
