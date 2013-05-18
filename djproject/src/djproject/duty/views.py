#coding=utf-8#
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.duty.models import Duty
from djproject.project.models import Project
import djproject.project.views as projectView

def duty_json(request):
    duty_all = Duty.objects.all()#TODO:Need custom class for serialization.
    duty_list = []
    for x in range(0,len(duty_all)):
        duty_list.append({
                          'name':duty_all[x].name,
                          'project':duty_all[x].project.name,
                          'month':duty_all[x].month,
                          'classes':duty_all[x].classes,
                          'days':duty_all[x].days,
                        })
#    print("duty_list:"+str(duty_list))
    return HttpResponse(simplejson.dumps(duty_list,ensure_ascii=True))

def duty_list(request):
    #Model
    projects = projectView.getProjects()
    rootMenus = projectView.getTreeMenusRoot()
    return render_to_response(
                                'duty/duty_list.html',
                                dictionary={
                                            'projects':projects,
                                            'rootMenus':rootMenus
                                            },
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