#coding=utf-8#

from django.contrib import admin
from djproject.employees.models import Department, Employee, Attendance, Salary, SalaryStatement

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(SalaryStatement)
