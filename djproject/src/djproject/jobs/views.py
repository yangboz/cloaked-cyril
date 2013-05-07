# Create your views here.
#from django.http import HttpResponse

#from django.template import Context,loader
from models import Job

from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpRequest
from django.http import HttpResponse

from django.utils import simplejson

def menus(request,):
    return render_to_response('basemenu.html')

def contact(request):
    return render_to_response('contacts/contact_new.html')

def json(request):
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


def index(request):
#    return HttpResponse("Hello world,you are the job index view.")
#    object_list = Job.objects.order_by('-pub_date')[:10]
    object_list = [
        {"id":"1","invdate":"2007-10-01","name":"test","note":"note","amount":"200.00","tax":"10.00","total":"210.00"},
        {"id":"2","invdate":"2007-10-02","name":"test2","note":"note2","amount":"300.00","tax":"20.00","total":"320.00"},
        {"id":"3","invdate":"2007-09-01","name":"test3","note":"note3","amount":"400.00","tax":"30.00","total":"430.00"},
        {"id":"4","invdate":"2007-10-04","name":"test","note":"note","amount":"200.00","tax":"10.00","total":"210.00"},
        {"id":"5","invdate":"2007-10-05","name":"test2","note":"note2","amount":"300.00","tax":"20.00","total":"320.00"},
        {"id":"6","invdate":"2007-09-06","name":"test3","note":"note3","amount":"400.00","tax":"30.00","total":"430.00"},
        {"id":"7","invdate":"2007-10-04","name":"test","note":"note","amount":"200.00","tax":"10.00","total":"210.00"},
        {"id":"8","invdate":"2007-10-03","name":"test2","note":"note2","amount":"300.00","tax":"20.00","total":"320.00"},
        {"id":"9","invdate":"2007-09-01","name":"test3","note":"note3","amount":"400.00","tax":"30.00","total":"430.00"}
        ]
#    t = loader.get_template('jobs/job_list.html')
#    c = Context({'object_list':object_list})
#    return HttpResponse(t.render(c))
    
    return render_to_response('jobs/job_list.html',{'object_list':object_list})

def detail(request,job_id):
    job = get_object_or_404(Job,pk=job_id)
    return render_to_response('jobs/job_detail.html',{'object':job})
