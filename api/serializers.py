from rest_framework import serializers
from .models import Movie, Review, List
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# Register
class RegisterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'username', 'email', 'password')
        extra_kwarg = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User.objects.create_user(
            validate_data['username'],
            validate_data['email'],
            validate_data['password'])

        return user

# Login
class LoginSerialiser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")