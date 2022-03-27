from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BoxModel, FileModel


class BoxSerializer(serializers.ModelSerializer):
    '''Box Serializer'''
    files = serializers.SerializerMethodField()
    def get_files(self, obj):
        return [obj_file.file.name for obj_file in obj.box_files.all()]

    class Meta:
        model = BoxModel
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    '''File Serializer'''
    class Meta:
        model = FileModel
        fields = '__all__'


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