from rest_framework import serializers
from django.contrib.auth.models import User
from .models import employee
# Serializer for input data (request)
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id','name', 'email', 'age', 'position', 'password1', 'password2']



    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Specify the fields you want to include