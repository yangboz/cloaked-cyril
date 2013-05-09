# Create your views here.
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.employees.models import Employee, Department

def index(request,projectId):
    # Session it
    request.session['projectId'] = projectId
    print "request.session.projectId:"+request.session['projectId']
    context = RequestContext(request)
    context['session_projectId'] = projectId
    # Access projectId with 'projectId' variable 
    return render_to_response('project/project_index.html',
                              dictionary={'projectId': projectId},
                              context_instance=context)
    
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
    return render_to_response('contacts/contact_list.html')


def contact_new(request):
	name = request.GET['name']

	e = Employee(name=name, department_id=1, laborCost=1, sex=True, contact="contact", notes="this is notes")
	e.save()

	return HttpResponse(Employee.objects.filter(name=name))

