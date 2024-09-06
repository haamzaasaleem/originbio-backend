from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from django.contrib.auth import get_user_model

User=get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom data to the response
        data.update({
            'username': self.user.username
            })

        return data

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',

            ]


