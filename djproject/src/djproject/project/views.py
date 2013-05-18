# coding = UTF-8
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.employees.models import Employee, Department
from djproject.project.models import Project
from djproject import settings

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate,login,logout
import os
#from djproject.project.forms import MyPhotoForm
from djproject.project.models import MyPhoto

from treemenus.models import Menu

from django.utils.log import getLogger
logger = getLogger('project.views')

@csrf_exempt
def login_view(request):    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)    
#        print("request.user"+str(user))    
        mimetype = "application/json";
        username = request.POST['username']
        # Session it
        request.session['username'] = username
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
    # Model
    rootMenus = getTreeMenusRoot()
    # Context
    context = RequestContext(request)
    # Access projectId with 'projectId' variable 
    return render_to_response('project/project_index.html',
                              dictionary={
                                          'projects':projects,
                                          'rootMenus':rootMenus
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
    
@csrf_exempt
def getProjectId(request):
    #@see:http://www.lichun.cc/blog/2012/06/a-simple-ajax-example-on-django-1-4/
    if request.is_ajax() and request.method == "GET":
        mimetype = "application/json";
        #if session kept.
        projectId = request.session['projectId']
        if projectId is None:
            projects = getProjects()
            # Session it with default value.
            projectId = projects[0].year
        print(" getProjectId:"+projectId)
        return HttpResponse(simplejson.dumps(projectId), mimetype);
    else:
        return HttpResponse("This is not an valid request");

def getProjects():
    # Model
    projects = Project.objects.all()
    print "projects:"+str(projects)
    return projects

@csrf_exempt
def setTreeMenusRootId(request):
    #@see:http://www.lichun.cc/blog/2012/06/a-simple-ajax-example-on-django-1-4/
    if request.is_ajax() and request.method == "POST":
        mimetype = "application/json";
        request.session['treeMenuRootId'] =  request.POST["treeMenuRootId"]
        print(" request.session.treeMenuRootId:"+request.session['treeMenuRootId'])
        return HttpResponse(request.session['treeMenuRootId'], mimetype);
    else:
        return HttpResponse("This is not an valid request");

def getTreeMenusRoot():
    # Model
    menuModel = Menu.objects.all()
    rootMenus = []
    for x in range(0,len(menuModel)-1):
        rootMenus.append(menuModel[x].name)
    print("rootMenus:"+str(rootMenus))
    return rootMenus

def projects(request):
    projects = getProjects()
    # Session it with default value.
    projectId = projects[0].name
    request.session['projectId'] = projectId
    print "request.session.projectId:"+request.session['projectId']
    # Context
    context = RequestContext(request)
    context['session_projectId'] = projectId
    # Access projectId with 'projectId' variable 
    return render_to_response('project/projects.html',
                              {
                                          'projectId': projectId,
                                          'projects':projects
                              },
                              context_instance=context)

def project(request):
    return render_to_response('project/project.html')

def contacts(request):
    return render_to_response('project/contacts.html')

def file(request):
    return render_to_response('project/file.html')

@csrf_exempt
def uploadFile(request):
    if request.method == 'POST':
       print 'filename' in request.FILES
       file = request.FILES.get('filename','')

       filename=file.name

       fname = os.path.join(settings.MEDIA_ROOT,filename)

       if os.path.exists(fname):  
         os.remove(fname)

         dirs= os.path.dirname(fname) 

         if not os.path.exists(dirs):  
            os.makedirs(dirs)  

       if os.path.isfile(fname): 
             os.remove(fname) 
 

       fp = open(fname, 'wb')  

       for content in file.chunks(): 

         fp.write(content)

       fp.close()

    return HttpResponse('ok')

def photo(request):
    return render_to_response('project/uploadPhoto.html')

@csrf_exempt
def uploadPhoto(request):

    print request.FILES
    print 'filename' in request.FILES
    if 'filename' in request.FILES:  
        image = request.FILES["filename"]

    else:
        image=None

    photo = MyPhoto(image=image)
    photo.save()

    return render_to_response('project/uploadedPhoto.html', {'photo':photo})