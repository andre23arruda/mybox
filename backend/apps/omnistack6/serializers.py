from django.contrib.auth.models import User
from rest_framework import serializers
from .models import FileModel


class FileSerializer(serializers.ModelSerializer):
    '''File Serializer'''
    class Meta:
        model = FileModel
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user