#coding=utf-8#

from django.db import models

#项目
class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    year = models.IntegerField()

    def __unicode__(self):
        return "Project_" + self.name



class MyPhoto(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos')

	