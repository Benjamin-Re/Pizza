# A model is a python class that maps to a database table

from django.db import models

# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=64)
	price = models.IntegerField()
	def __str__(self):
		return f"Regular Pizza {self.name} costs {self.price}€."
	
	