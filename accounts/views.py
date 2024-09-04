from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from accounts.serializer import UserModelSerializer
# Create your views here.

User=get_user_model()


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
