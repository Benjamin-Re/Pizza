# A view is a python function that takes a web request and returns a web response

from django.http import HttpResponse
from django.shortcuts import render, Http404
# have to import the class Pizza from the model so can pass its instances to template
from orders.models import Pizza, Topping, ShoppingCart

# This is imported for the signup_functionality
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def index(request):
    # the context dictionary passes on data to a template to be used with templating language
    context = {
        "pizzas": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # lazy bc have to wait for template to load ?!
    template_name = 'signup.html'

def pizza(request, pizza_id): #the id is provided as parameter
    try:
        pizza = Pizza.objects.get(pk=pizza_id) # get me the pizza with corresponding id
    except Pizza.DoesNotExist:
        raise Http404("This pizza does not exist")
    context = {
        "pizza": pizza,
		"toppings": Topping.objects.all()
    }
    return render(request, "orders/pizza.html", context)

def addToCart(request, pizza_id):
	pizza = Pizza.objects.get(pk=pizza_id) # make a pizza instance with pk we get as parameter from the page i guess
	pizza.save()
	try: # see if a shopping cart for this user already exists
		shoppingCartInstance = ShoppingCart.objects.get(buyer=request.user)
		shoppingCartInstance.save()
	except ShoppingCart.DoesNotExist: # if it doesnt exist already create one
		shoppingCartInstance = ShoppingCart.objects.create(buyer=request.user)
		shoppingCartInstance.save()
	shoppingCartInstance.item.add(pizza) # add the pizza instance to the shoppingcartinstance. Later also quantity
	return HttpResponse('Added item to shopping Cart!') #this should be a page displaying the items in the shoppin Cart

def addToPizza(request, pizza_id, topping_id):
	pizza = Pizza.objects.get(pk=pizza_id)
	topping = Topping.objects.get(pk=topping_id)
	try:
		pizza.topping.add(topping)
	except Topping.DoesNotExist:
		return Http404('Topping does not exist')
	except Pizza.DoesNotExist:
		return Http404('Pizza does not exist')
	return HttpResponse('Added topping to your pizza')
	
def show(request, cart_id): #the id is provided as parameter
    try:
        currentShoppingCart = ShoppingCart.objects.get(pk=cart_id) # get me the pizza with corresponding id
    except ShoppingCart.DoesNotExist:
        raise Http404("This ShoppingCart does not exist")
    context = {
        "shoppingCart": currentShoppingCart
    }
    return render(request, "orders/show.html", context)
	