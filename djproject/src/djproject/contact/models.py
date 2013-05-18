from django.db import models

from djproject.project.models import Project
from djproject.duty.models import Duty
from djproject.employees.models import Employee,Salary,SalaryStatement
# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(max_length=200, blank=False)
    project = models.ForeignKey(Project)
    duty = models.ForeignKey(Duty)
    employee = models.ForeignKey(Employee)
    salary = models.ForeignKey(Salary)
    salaryStatement = models.ForeignKey(SalaryStatement)
    
    def __unicode__(self):
        return "Contact_" + self.name