# A model is a python class that maps to a database table

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=64)
	price = models.IntegerField()
	topping = models.ManyToManyField('Topping', through='ToppingAmount', related_name='pizzas', default='none')
	def __str__(self):
		helper = ", ".join(str(seg) for seg in self.topping.all())
		return f"Pizza: {self.name}, Price: {self.price}, Toppings: {helper}."

class ShoppingCart(models.Model):
	buyer = models.ForeignKey(User, on_delete=models.CASCADE, default = 'newUser')
	item = models.ManyToManyField(Pizza, related_name="shoppingCarts")
	def __str__(self):
		helper = ", ".join(str(seg) for seg in self.item.all())
		test = self.item.all()
		return f"Shopper {self.buyer} added {helper} to shopping cart."
	
class Topping(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return self.name
		
# Through Model
class ToppingAmount(models.Model):
    # This magic allows .remove() to be used on the manyToMany Relationship, although a through model was implemented
    class Meta:
        auto_created = True
    pizza = models.ForeignKey('Pizza', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
    topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(default=0)
  
	
