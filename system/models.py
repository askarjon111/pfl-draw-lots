from django.db import models

class Team(models.Model):
	title = models.TextField(null = True)
	logo = models.ImageField(upload_to = 'media/', null = True ,blank = True)
	num = models.TextField(null = True)

	def __str__(self):
		return self.title
	