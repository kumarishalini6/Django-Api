from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'contact_no' ]

admin.site.register(Employee, EmployeeAdmin)