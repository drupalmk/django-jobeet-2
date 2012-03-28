from django.conf.urls import patterns, include, url
from jobeet import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','jobs.views.index', name='index'),
    url(r'^jobs/$', 'jobs.views.index'),
    url(r'^jobs/(?P<id>\d+)/show$', 'jobs.views.show_job'),
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root', settings.STATIC_ROOT}
    ),

    # Examples:
    # url(r'^$', 'jobeet.views.home', name='home'),
    # url(r'^jobeet/', include('jobeet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
