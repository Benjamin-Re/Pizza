# A view is a python function that takes a web request and returns a web response

from django.http import HttpResponse
from django.shortcuts import render, Http404
# have to import the class Pizza from the model so can pass its instances to template
from orders.models import Pizza

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
    }
    return render(request, "orders/pizza.html", context)

