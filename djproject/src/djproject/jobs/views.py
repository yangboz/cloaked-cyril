# Create your views here.
from django.http import HttpResponse

from django.template import Context,loader
from models import Job

from django.shortcuts import get_object_or_404,render_to_response

def index(request):
#    return HttpResponse("Hello world,you are the job index view.")
    object_list = Job.objects.order_by('-pub_date')[:10]
#    t = loader.get_template('jobs/job_list.html')
#    c = Context({'object_list':object_list})
#    return HttpResponse(t.render(c))
    return render_to_response('jobs/job_list.html',{'object_list':object_list})

def detail(request,object_id):
    job = get_object_or_404(Job,pk=object_id)
    return render_to_response('jobs/job_detail.html',{'object':job})
