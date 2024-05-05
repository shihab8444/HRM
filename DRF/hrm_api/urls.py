
from django.urls import path
from .views import EmployeeAPIView,EmployeeFind,Employee_by_Department
urlpatterns = [
    path('myform/', EmployeeAPIView.as_view(), name='myform'),
    path('myform/<int:pk>/', EmployeeFind.as_view(), name='employee'),
    path('myform/department/<str:department_name>/', Employee_by_Department.as_view(), name='department'),
    

]
