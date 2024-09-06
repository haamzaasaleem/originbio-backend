from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from accounts.serializer import UserModelSerializer,CustomTokenObtainPairSerializer


# Create your views here.

User=get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserCrudView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
