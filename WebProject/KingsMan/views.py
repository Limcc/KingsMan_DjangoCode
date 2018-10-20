from django.shortcuts import render
from django.http import HttpResponse
from .models import product

# Create your views here.

def index(request):
    db = product.objects.get(category="set")
    dic = {"path": db.photo, "name": db.name, "price": db.price}
    return render(request, "KingsMan.html", dic)

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

def search(request):
    return render(request, "search.html")

def cart(request):
    return render(request, "cart.html")

def question(request):
    return render(request, "question.html")

def login(request):
    return render(request, "login.html")

def join(request):
    return render(request, "join.html")

def game(request):
    return render(request, "game.html")