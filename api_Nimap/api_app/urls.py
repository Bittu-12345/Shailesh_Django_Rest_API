
from django.urls import path
from .views import Create_clients,Update_del_clients,Create_projects,Update_del_projects,Create_user,Update_del_user

urlpatterns = [
    path('clients/', Create_clients.as_view(), name='create-clients'),
    path('clients/<int:pk>/', Update_del_clients.as_view(), name='update-delete-clients'),
    path('projects/', Create_projects.as_view(), name='create-projects'),
    path('projects/<int:pk>/', Update_del_projects.as_view(), name='update-delete-projects'),
    path('users/', Create_user.as_view(), name='create-users'),
    path('users/<int:pk>/', Update_del_user.as_view(), name='update-delete-users'),
]

