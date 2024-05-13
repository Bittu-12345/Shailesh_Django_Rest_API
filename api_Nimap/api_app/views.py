# project_manager_app/views.py
from rest_framework import generics
from .models import Client, Project
from .serializers import Client_S, Project_S, User_S
from .models import User

class Create_user(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_S

class Update_del_user(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_S

class Create_clients(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_S

class Update_del_clients(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_S

class Create_projects(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_S

class Update_del_projects(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_S