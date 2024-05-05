from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import MyForm
from .serializers import  EmployeeSerializer  

from .models import employee
class EmployeeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize input data
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            # Process valid input data
            # name = serializer.validated_data['name']
            # email = serializer.validated_data['email']
            # age = serializer.validated_data.get('age')
            # position = serializer.validated_data.get('position')          
            # password1 = serializer.validated_data.get('password1')
            # password2 = serializer.validated_data.get('password2')
            # print(name)
            # print(email)
            # print(age)
            # print(position)
            # print(password1)
            # print(password2)
            
            # Process form data
            form = MyForm(data=request.data)  # Pass request data here
            
            if form.is_valid():
                # If form is valid, no need to access cleaned_data directly
                # You can directly access validated fields from the form
                # print('clean_data', form.cleaned_data['name'])
                # print('clean_data', form.cleaned_data['email'])

                # Serialize form data to JSON
                form.save()
                json_data_form = serializer.data
                return Response(json_data_form, status=status.HTTP_201_CREATED)
            
            # Form validation failed
            return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        # Input data validation failed
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, format=None):
        employees = employee.objects.exclude(password1='',password2='').values('id','name', 'email', 'age', 'position')
        serializer = EmployeeSerializer(employees, many=True)
        # print('json ',serializer)
        return Response(serializer.data)




class EmployeeFind(APIView):
    def get(self, request, pk, format=None):
        try:
            employee_instance = employee.objects.get(pk=pk)
            
            serializer = EmployeeSerializer(employee_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except employee.DoesNotExist:
            return Response({"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

            



class Employee_by_Department(APIView):

     def get(self, request, department_name, format=None):
        try:
            # Filter employees based on department name
            employees = employee.objects.filter(department__Dname__iexact=department_name)
            # print(employees)
            # Serialize the filtered employees
            serializer = EmployeeSerializer(employees, many=True)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except employee.DoesNotExist:
            return Response({'message': 'No employees found for the specified department'}, status=status.HTTP_404_NOT_FOUND)


