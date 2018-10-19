from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "KingsMan.html")

def outer(request):
    return temp(request, "outer")

def shirts(request):
    return temp(request, "shirts")

def pants(request):
    return temp(request, "pants")

def shoes(request):
    return temp(request, "shoes")

def accessory(request):
    return temp(request, "accessory")

def temp(request, category):
    return render(request, "template.html", {"category": category})