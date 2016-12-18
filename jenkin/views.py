from django.shortcuts import render
from django.http import HttpResponse
from .models import JenkinsJob
import jenkins


# Create your views here.e
def index(request):
	server = jenkins.Jenkins('http://localhost:8080/', username='ify2', password='d2044cf3be0052c2064617302ea264ad')
	jobs = server.get_jobs()
	job_status = {
	'blue': 'Successfull',
	'red': 'notSuccessfull',
	'notbuilt': 'notBuilt'
	}
	for job in jobs:
		JenkinsJob.objects.create(name=job['name'], status=job_status[job['color']])
	# print('Hello %s from Jenkins %s' % (user['fullName'], version))
	print(JenkinsJob.objects.all())
	return HttpResponse("Hello, World. You're at the polls index")