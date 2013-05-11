from django.db import models

from djproject.project.models import Project
# Create your models here.

class Duty(models.Model):
    name = models.CharField(max_length=200, blank=False)
    project = models.ForeignKey(Project)
    month = models.IntegerField(max_length=2,blank=False)
    classes = models.IntegerField(max_length=9999,blank=False)
    days = models.CommaSeparatedIntegerField(max_length=70)

    def __unicode__(self):
        return "Duty_" + self.name