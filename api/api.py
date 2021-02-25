from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerialiser, UserSerializer, LoginSerialiser

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerialiser

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user,
            context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[-1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerialiser

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": UserSerializer(user,
            context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[-1]
        })