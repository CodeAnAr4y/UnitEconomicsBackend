from rest_framework import serializers  
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate  


class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ('id', 'username', 'email')  


class RegisterSerializer(serializers.ModelSerializer):  
    password = serializers.CharField(write_only=True)  

    class Meta:  
        model = User  
        fields = ('username', 'email', 'password')  

    def create(self, validated_data):  
        user = User(  
            username=validated_data['username'],  
            email=validated_data['email'],  
        )  
        user.set_password(validated_data['password'])
        user.save()  
        return user  


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        data['user'] = user
        return data