#coding=utf-8#

from django.db import models
from djproject.project.models import Project
from datetime import date

#部门
class Department(models.Model):
    name = models.CharField(max_length=200, blank=False)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return "Department_" + self.name + self.project.name

#员工
class Labor(models.Model):
    name = models.CharField(max_length=20, blank=False)
    department = models.ForeignKey(Department)
    sex = models.BooleanField()
    job = models.CharField(max_length=200)
    laborCost = models.IntegerField()
    IDCard = models.CharField(max_length=50)
    contactWay = models.CharField(max_length=300)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "Labor_" + self.name

#出勤
class Attendance(models.Model):
    labor = models.ForeignKey(Labor)
    year = models.IntegerField(date.today().year)
    month = models.IntegerField(date.today().month)
    attend = models.CommaSeparatedIntegerField(max_length=100)

    def __unicode__(self):
        return "Attendance_" + self.labor.name + self.year + self.month

#工资
class Salary(models.Model):
    labor = models.ForeignKey(Labor)
    year = models.IntegerField(date.today().year)
    month = models.IntegerField(date.today().month)
    salary = models.IntegerField()
    actualSalary = models.IntegerField()

    def __unicode__(self):
        return "Salary_" + self.labor.name + self.year + self.month

#工资出账单
class SalaryStatement(models.Model):
    labor = models.ForeignKey(Labor)
    arriveDate = models.DateField()
    leaveDate = models.DateField()
    attachment = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "SalaryStatement_" + self.labor.name
