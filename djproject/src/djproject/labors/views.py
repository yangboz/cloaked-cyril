
from django.contrib import admin
from djproject.labors.models import Department, Labor, Attendance, Salary, SalaryStatement

admin.site.register(Department)
admin.site.register(Labor)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(SalaryStatement)# Create your views here.
