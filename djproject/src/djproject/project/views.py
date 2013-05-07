# Create your views here.
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

def index(request,projectId):
    # Access projectId with 'projectId' variable 
    return render_to_response('project/project_index.html',
                              dictionary={'projectId': projectId},
                              context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contacts/contact_new.html')