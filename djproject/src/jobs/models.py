from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(maxlength=50)
    state = models.CharField(maxlength=50,null=True,blank=True)
    country = models.CharField(maxlength=50)
    
    def __str__(self):
        if self.state:
            return "%s,%s,%s" %(self.city,self.state,self.country)