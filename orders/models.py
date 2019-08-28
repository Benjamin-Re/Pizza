from django.db import models

# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=64)
	LARGE = 'l'
	SMALL = 's'
	SIZES = [
		('l', 'large'),
		('s', 'small'),
	]
	size = models.CharField(max_length=1, choices=SIZES, default='l')
	# large = models.BooleanField(default=True)
	price = models.IntegerField()
	def __str__(self):
		return f"Regular Pizza {self.name}, {self.size} costs {self.price}" 
	
	