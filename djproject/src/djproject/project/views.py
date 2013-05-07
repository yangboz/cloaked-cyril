# Create your views here.
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse

from django.utils import simplejson

def index(request):
    return render_to_response('project/project_index.html')

def contact(request):
    return render_to_response('contacts/contact_new.html')