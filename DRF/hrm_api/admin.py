from django.contrib import admin
from .models import employee,Department
# Register your models here.

@admin.register(employee)
class employee_detail(admin.ModelAdmin):
    list_display=('id','name','email')

@admin.register(Department)
class department_detail(admin.ModelAdmin):
    list_display=('id','department_name') 
    
    def department_name(self,obj):
        return obj.Dname
    
    department_name.short_description ='department Name'