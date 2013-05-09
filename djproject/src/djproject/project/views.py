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

def contact_list(request):
    return render_to_response('contacts/contact_list.html')


def contact_new(request):
	name = request.GET['name']

	e = Employee(name=name, department_id=1, laborCost=1, sex=True, contact="contact", notes="this is notes")
	e.save()

	return HttpResponse(Employee.objects.filter(name=name))

