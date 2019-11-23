# A view is a python function that takes a web request and returns a web response

from django.http import HttpResponse
from django.shortcuts import render, Http404
# have to import the class Pizza from the model so can pass its instances to template
from orders.models import Pizza, Topping, ShoppingCart, ToppingAmount

# This is imported for the signup_functionality
from django.contrib.auth.forms import UserCreationForm, User
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

# gets and displays one specific pizza
def pizza(request, pizza_id): #the id is provided as parameter
    try:
        pizza = Pizza.objects.get(pk=pizza_id) # get me the pizza with corresponding id
    except Pizza.DoesNotExist:
        raise Http404("This pizza does not exist")
    context = {
        "pizza": pizza,
		"toppings": Topping.objects.all(),
		"activeToppings": pizza.topping.all()
    }
    return render(request, "orders/pizza.html", context)

# gets a certain pizza and current user's shoppingCart and adds the pizza to the ShoppingCart
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
	return HttpResponse('Added item to shopping Cart! <br><a href="/showCart">Show ShoppingCart</a><br><a href="/">back</a>') #this should be a page displaying the items in the shoppin Cart

# adds a certain topping to a certain pizza
def addToPizza(request, pizza_id, topping_id):
	# Get current pizza and topping
	pizza = Pizza.objects.get(pk=pizza_id)
	topping = Topping.objects.get(pk=topping_id)
	try:
		# create a relation between the two with a through model
		t = ToppingAmount.objects.create(pizza=pizza, topping=topping, amount = 1)
		#pizza.topping.add(topping)
	except Topping.DoesNotExist:
		return Http404('Topping does not exist')
	except Pizza.DoesNotExist:
		return Http404('Pizza does not exist')
	context = {
        "pizzas": Pizza.objects.all()
    }
	return render(request, "orders/index.html", context) #ToDo: Id love to stay on the pizza page here, but linking to pizza.html gives an error.

# Shows current user's shoppingCart	
def show(request): 
    sum = 0
    try:
        currentShoppingCart = ShoppingCart.objects.get(buyer=request.user) # get me the ShoppingCart with current user
    except ShoppingCart.DoesNotExist:
        raise Http404("This ShoppingCart does not exist")
    items = currentShoppingCart.item.all()
    for item in items:
        sum = sum + item.price
    context = {
		"sum": sum,
        "ShoppingCart": currentShoppingCart,
		"items": items
    }
    return render(request, "orders/show.html", context)

# Deletes a certain item from current user's shoppingCart	
def delete(request, item_id):
	currentShoppingCart = ShoppingCart.objects.get(buyer=request.user) #first get the current shopper's cart
	item = currentShoppingCart.item.get(pk=item_id) # this works, checked in shell
	currentShoppingCart.item.remove(item)
	return HttpResponse('deleted item from shopping cart <br><a href="/">back</a>')

# Deletes a certain topping from a certain pizza	
def deleteTopping(request, pizza_id, topping_id):
	pizza = Pizza.objects.get(pk=pizza_id)
	topping = Topping.objects.get(pk=topping_id)
	# This erases all toppings of a certain kind from the pizza, i.e. it erases all instances of the through model
	pizza.topping.remove(topping)
	#t = pizza.objects.filter(pizza__topping=topping)
	#delete(t)
	# pizza.topping.remove(topping)
	# pizza.save()
	return HttpResponse('deleted topping from pizza <br><a href="/">back</a>')