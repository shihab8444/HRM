from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class Department(models.Model):
    Dname = models.CharField(max_length=100)  

  

    def __str__(self):
        return self.Dname 


class employee(models.Model):
        name=models.CharField( max_length=100)
        email = models.EmailField(max_length=100,default='')  
        age=models.IntegerField(default=0)
        position=models.CharField(max_length=100,default='')
        password1=models.CharField(max_length=100,default='')
        password2=models.CharField(max_length=100,default='')
        department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department',default=None, null=True)

        def __str__(self):
           return self.name




       
