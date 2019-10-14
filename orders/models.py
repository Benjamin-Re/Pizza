# A model is a python class that maps to a database table

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=64)
	price = models.IntegerField()
	topping = models.ManyToManyField('Topping', related_name='pizzas', default='none')
	def __str__(self):
		return f"Pizza: {self.name}, Price: {self.price}, Toppings: {self.topping}."

class ShoppingCart(models.Model):
	buyer = models.ForeignKey(User, on_delete=models.CASCADE, default = 'newUser')
	item = models.ManyToManyField(Pizza, related_name="shoppingCarts")
	def __str__(self):
		return f"Shopper {self.buyer} added {self.item} to shopping cart."

class Topping(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return self.name
