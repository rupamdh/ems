from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Designation)
# admin.site.register(Employee)


class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", "designation", "assigned_to",)
  
admin.site.register(Employee, EmployeeAdmin)