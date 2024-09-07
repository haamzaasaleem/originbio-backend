from django.shortcuts import render

from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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



class ResetPassword(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def post(self, request):
        new_password=request.POST['new_password']
        current_password=request.POST['current_password']
        confirm_password=request.POST['confirm_password']


        user=request.user
        if not user.check_password(current_password):
            return Response({"details":"Current Password is wrong"})
        
        if new_password != confirm_password:
            return Response({"details":"Password doesn't matched"})
        
        user.set_password(new_password)
        user.save()

        serializer=UserModelSerializer(user)
        return Response(serializer.data)


            





        


