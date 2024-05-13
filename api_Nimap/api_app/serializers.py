from rest_framework import serializers
from .models import User, Client, Project


class User_S(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'phone_number', 'address','Location_City','password']

class Client_S(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'contact', 'email', 'organization', 'location']

class Project_S(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'Project_name', 'client', 'users']