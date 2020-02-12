from django.db import models

# Create your models here.

class Contact(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __unicode__(self):
		return self.title