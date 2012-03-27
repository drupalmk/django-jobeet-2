from django.http import HttpResponse

def index(request):
    return HttpResponse("You're looking at jobs list")

def show_job(request, id):
    return HttpResponse("You're looking at the results of job %s." % id)