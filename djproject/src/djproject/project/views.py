# Create your views here.
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.employees.models import Employee, Department
from djproject.project.models import Project

from django.views.decorators.csrf import csrf_exempt

def index(request):
    projects = getProjects()
    # Session it with default value.
    projectId = projects[0].name
    request.session['projectId'] = projectId
    print "request.session.projectId:"+request.session['projectId']
    # Context
    context = RequestContext(request)
    context['session_projectId'] = projectId
    # Access projectId with 'projectId' variable 
    return render_to_response('project/project_index.html',
                              dictionary={
                                          'projectId': projectId,
                                          'projects':projects
                                          },
                              context_instance=context)
@csrf_exempt
def setProjectId(request):
    if request.is_ajax() and request.method == "POST":
        mimetype = "application/json";
        request.session['projectId'] =  request.POST["projectId"]
#        print(request.POST["projectId"])
        return HttpResponse(request.session['projectId'], mimetype);
    else:
        return HttpResponse("This is not an valid request");

def getProjects():
    # Model
    projects = Project.objects.all()
    print "projects:"+str(projects)
    return projects