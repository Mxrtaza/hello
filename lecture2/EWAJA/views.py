from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Drerrie")

def brian(request):
    return HttpResponse("Hello Brian")

def david(request):
    return HttpResponse("Hello David")

def murtaza(request):
    return HttpResponse("Hello Murtaza")

def greet(request, name):
    return HttpResponse(f"Hello,{name.capitalize()}")



