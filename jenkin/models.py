from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class JenkinsJob(models.Model):
	name = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	check_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name
		