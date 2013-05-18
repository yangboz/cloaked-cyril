from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.http import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^djproject/', include('djproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^admin/', include(admin.site.urls)),
    
    (r'^jobs/$', 'djproject.jobs.views.index'),
    (r'^json/$', 'djproject.jobs.views.json'),
    (r'^menus/$', 'djproject.jobs.views.menus'),
    (r'^jobs/(?P<job_id>\d+)/$', 'djproject.jobs.views.detail'),
    (r'^jobs/', include('djproject.jobs.urls')),
    (r'^project/$', 'djproject.project.views.index'),
    (r'^project/setProjectId/$', 'djproject.project.views.setProjectId'),
    (r'^project/getProjectId/$', 'djproject.project.views.getProjectId'),
    (r'^contact/contact_new/$', 'djproject.contact.views.contact_new'),
    (r'^contact/contact_list/$', 'djproject.contact.views.contact_list'),
    (r'^contact/contact_json/$', 'djproject.contact.views.contact_json'),
    (r'^duty/duty_new/$', 'djproject.duty.views.duty_new'),
    (r'^duty/duty_list/$', 'djproject.duty.views.duty_list'),
    (r'^duty/duty_json/$', 'djproject.duty.views.duty_json'),
    (r'^project/login/$', 'djproject.project.views.login_view'),
    (r'^project/logout/$', 'djproject.project.views.logout_view'),
    (r'^project/projects/$', 'djproject.project.views.projects'),
    (r'^project/project/$', 'djproject.project.views.project'),
    (r'^project/contacts/$', 'djproject.project.views.contacts'),
    (r'^project/contacts/contact_new/$', 'djproject.contact.views.contact_new'),
    (r'^project/contacts/uploadfile/$', 'djproject.project.views.uploadFile'),
    (r'^project/contacts/file/$', 'djproject.project.views.file'),
    (r'^project/contacts/uploadPhoto/$', 'djproject.project.views.uploadPhoto'),
    (r'^project/contacts/photo/$', 'djproject.project.views.photo'),
    (r'^project/setTreeMenusRootId/$', 'djproject.project.views.setTreeMenusRootId'),
    (r'^project/contacts/photo/$', 'djproject.project.views.photo'),
    (r'^project/getTreeMenusRootId/$', 'djproject.project.views.getTreeMenusRootId'),
)

urlpatterns += staticfiles_urlpatterns()