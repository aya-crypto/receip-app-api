from django.shortcuts import render

from rest_framework import generics ,authentication ,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer ,AuthTokenSerializer
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """create new user in system"""
    serializer_class =UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create new Token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManagerUserView(generics.RetrieveUpdateAPIView):
    """manage the authenticated user."""
    serializer_class =UserSerializer
    authenication_classess = (authentication.TokenAuthentication,)
    permission_classess =(permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
