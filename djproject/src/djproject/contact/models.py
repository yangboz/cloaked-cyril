from django.db import models

from djproject.project.models import Project
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False)
    project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return "Duty_" + self.name