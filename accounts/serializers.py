from django.shortcuts import render
from . models import Account, App, completedTask 
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ListField
import re
from rest_framework import serializers

# Create your views here.


class AccountSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style={'input':'password2'},write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        expect="password"
        fields = ['id','first_name', 'last_name', 'username', 'email','phone_number', 'password', 'password2' ]
        # extra_kwargs = {'password': {'write_only': True}}
    def save(self):
        register=Account(
          username=self.validated_data["username"],
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            phone_number=self.validated_data["phone_number"],
            )
        password=self.validated_data["password"]
        print(password)
        password2=self.validated_data["password2"]
        print(password2)
        if password != password2:
            raise serializers.ValidationError({'password':'password dosent match'})
        print(password)
        print(type(password))
        
        register.set_password(password)
        print("jjjjjjjjjjjjjj")
        register.save()
        return register
class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Account
        fields=  '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields=  '__all__'   

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = completedTask
        fields=  '__all__'
        depth = 1


class completedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = completedTask
        fields=  '__all__' 

