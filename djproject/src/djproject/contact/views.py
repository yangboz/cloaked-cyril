# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.labors.models import Labor
from djproject.contact.models import Contact
import djproject.project.views as projectView

def contact_json(request):
    object_list = [
        {"id":"1","name":"2007-5-4","sex":"test","job":"note","laborCost":"200.00","IDcard":"10.00","contact":"210.00","notes":"some notes"},
        {"id":"2","name":"2007-10-02","sex":"test2","job":"note2","laborCost":"300.00","IDcard":"20.00","contact":"320.00","notes":"some notes"},
        {"id":"3","name":"2007-09-01","sex":"test3","job":"note3","laborCost":"400.00","IDcard":"30.00","contact":"430.00","notes":"some notes"},
        {"id":"4","name":"2007-10-04","sex":"test","job":"note","laborCost":"200.00","IDcard":"10.00","contact":"210.00","notes":"some notes"},
        {"id":"5","name":"2007-10-05","sex":"test2","job":"note2","laborCost":"300.00","IDcard":"20.00","contact":"320.00","notes":"some notes"},
        {"id":"6","name":"2007-09-06","sex":"test3","job":"note3","laborCost":"400.00","IDcard":"30.00","contact":"430.00","notes":"some notes"},
        {"id":"7","name":"2007-10-04","sex":"test","job":"note","laborCost":"200.00","IDcard":"10.00","contact":"210.00","notes":"some notes"},
        {"id":"8","name":"2007-10-03","sex":"test2","job":"note2","laborCost":"300.00","IDcard":"20.00","contact":"320.00","notes":"some notes"},
        {"id":"9","name":"2007-09-01","sex":"test3","job":"note3","laborCost":"400.00","IDcard":"30.00","contact":"430.00","notes":"some notes"}
    ]
    
    return HttpResponse(simplejson.dumps(object_list))

def contact_list(request):
    projects = projectView.getProjects()
    rootMenus = projectView.getTreeMenusRoot()
    return render_to_response(
                                'contacts/contact_list.html',
                                dictionary={
                                            'projects':projects,
                                            'rootMenus':rootMenus
                                            },
                                context_instance=RequestContext(request)
                              )


def contact_new(request):
    name = request.GET['name']

    labor = Labor(name=name, department_id=1, laborCost=1, sex=True, contact="contact", notes="this is notes")
    labor.save()

    return HttpResponse(Labor.objects.filter(name=name))