# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django.utils import simplejson

from djproject.labors.models import Labor
from djproject.contact.models import Contact
import djproject.project.views as projectView

def contact_json(request):
    contact_model = Contact.objects.all()
    contact_list = []
    for x in range(0,len(contact_model)):
        contact_list.append(
                            {
                             'id':contact_model[x].id,
                             'name':contact_model[x].name,
                             'sex':contact_model[x].sex,
                             'job':contact_model[x].job,
                             'laborCost':contact_model[x].laborCost,
                             'IDCard':contact_model[x].idCard,
                             'notes':contact_model[x].notes
                             }
                            )
    
    return HttpResponse(simplejson.dumps(contact_list,ensure_ascii=True))

def contact_list(request):
    projects = projectView.getProjects()
    rootMenus = projectView.getTreeMenusRoot()
    return render_to_response(
                                'contacts/contact_list.html',
                                dictionary={
                                            'projects':projects,
                                            'rootMenus':rootMenus
                                            },
                                context_instance=RequestContext(request)
                              )


def contact_new(request):
    name = request.GET['name']

    labor = Labor(name=name, department_id=1, laborCost=1, sex=True, contact="contact", notes="this is notes")
    labor.save()

    return HttpResponse(Labor.objects.filter(name=name))