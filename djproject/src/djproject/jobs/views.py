# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world,you are the job index view.")
