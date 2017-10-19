from django.db import models # plus other files
from django.utils import timezone


#class : define object  #Post : name of model
class Post(models.Model): # define models, model is object
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title
