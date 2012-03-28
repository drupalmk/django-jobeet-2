from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from jobs.models import *

def index(request):

  categories = Categories.objects.get_with_jobs()

  from jobeet import settings
  for category in categories:
    category.active_jobs = Jobs.objects.get_active_by_category(category, settings.MAX_JOBS_BY_CATEGORY)

  return render_to_response('index.html', {'categories': categories}, context_instance=RequestContext(request))

def show_job(request, id):
    return HttpResponse("You're looking at the results of job %s." % id)