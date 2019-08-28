# A view is a python function that takes a web request and returns a web response

from django.http import HttpResponse
from django.shortcuts import render
# have to import the class Pizza from the model so can pass its instances to template
from orders.models import Pizza


# Create your views here.

def index(request):
    # the context dictionary passes on data to a template to be used with templating language
    context = {
        "pizzas": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)
