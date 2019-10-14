from django.contrib import admin
from .models import Pizza, ShoppingCart, Topping

# Register your models here.
admin.site.register(Pizza)
admin.site.register(ShoppingCart)
admin.site.register(Topping)