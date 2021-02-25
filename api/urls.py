from django.urls import path, include
from rest_framework import routers
from .views import *

from .api import RegisterAPI, LoginAPI
from knox import views as knox_views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'lists', ListViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
