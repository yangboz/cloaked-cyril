# Create your views here.
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.employees.models import Employee, Department
from djproject.project.models import Project

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate,login,logout

@csrf_exempt
def login_view(request):    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)    
#        print("request.user"+str(user))    
        mimetype = "application/json";
        username = request.POST['username']
        return HttpResponse(simplejson.dumps(username), mimetype);
    else:
        #Empty handler
        return HttpResponse(status=404)
    
@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse(status=204)

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
    #@see:http://www.lichun.cc/blog/2012/06/a-simple-ajax-example-on-django-1-4/
    if request.is_ajax() and request.method == "POST":
        mimetype = "application/json";
        request.session['projectId'] =  request.POST["projectId"]
        print(" request.session.projectId:"+request.session['projectId'])
        return HttpResponse(request.session['projectId'], mimetype);
    else:
        return HttpResponse("This is not an valid request");

def getProjects():
    # Model
    projects = Project.objects.all()
    print "projects:"+str(projects)
    return projects