from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True)
    name= models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255,null=True)
    Location_City = models.CharField(max_length=255,null=True)
    
    class Meta:
        db_table = 'custom_user'

# Add custom related_name arguments for the groups and user_permissions fields
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_permissions')

class Client(models.Model):
    name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    email = models.EmailField()
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Project(models.Model):
    Project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')
    def __str__(self):
        return self.Project_name