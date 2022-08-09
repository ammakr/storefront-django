from itertools import product
from django.shortcuts import render
from store.models import OrderItem, Product

def say_hello(request):
         
    return render(request, 'hello.html', {'name': 'Mosh'})
