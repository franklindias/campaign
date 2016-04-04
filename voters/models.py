from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=100)
	indication = models.ForeignKey('Person', blank=True, null=True)

	def __str__(self):
		return self.name