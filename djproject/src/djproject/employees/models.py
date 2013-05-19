#coding=utf-8#

from django.db import models
from djproject.project.models import Project
from datetime import date


class Department(models.Model):
    name = models.CharField(max_length=200, blank=False)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return "Department_" + self.name

class Employee(models.Model):
    name = models.CharField(max_length=20, blank=False)
    department = models.ForeignKey(Department)
    sex = models.BooleanField()
    job = models.CharField(max_length=200)
    laborCost = models.IntegerField()
    IDCard = models.CharField(max_length=50)
    contactWay = models.CharField(max_length=300)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "Empolyee_" + self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateField(default=date.today())
    attend = models.BooleanField()

    def __unicode__(self):
        return "Attendance_" + self.employee.name + self.date


class Salary(models.Model):
    employee = models.ForeignKey(Employee)
    year = models.IntegerField(date.today().year)
    month = models.IntegerField(date.today().month)
    salary = models.IntegerField()
    actualSalary = models.IntegerField()

    def __unicode__(self):
        return "Salary_" + self.employee.name + self.year + self.month

class SalaryStatement(models.Model):
    employee = models.ForeignKey(Employee)
    arriveDate = models.DateField()
    leaveDate = models.DateField()
    attachment = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "SalaryStatement_" + self.employee.name
