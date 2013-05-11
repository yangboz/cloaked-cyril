# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.duty.models import Duty
from djproject.project.models import Project

def duty_json(request):
    duty_list = Duty.objects.all()
    return HttpResponse(simplejson.dumps(duty_list))

def duty_list(request):
    projects = getProjects()
    return render_to_response(
                                'duty/duty_list.html',
                                dictionary={'projects':projects},
                                context_instance=RequestContext(request)
                              )


def duty_new(request):
    #TODO:
    return HttpResponse(status=204)


def getProjects():
    # Model
    projects = Project.objects.all()
    print "projects:"+str(projects)
    return projects