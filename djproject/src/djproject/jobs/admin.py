from django.contrib import admin
from models import Location,Job

class JobAdmin(admin.ModelAdmin):
    fields = ['job_title','location','pub_date']

admin.site.register(Location)
admin.site.register(Job,JobAdmin)