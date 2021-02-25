from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, ListSerializer, MovieSerializer, ReviewSerializer
from .models import Movie, Review, List


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListViewSet(viewsets.ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = []

    # def get_queryset(self):
    #     user = self.request.user
    #     return self.queryset.filter(user=user)


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []


class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
