from django.shortcuts import render
from django.http import HttpResponse
from .models import product

# Create your views here.

def index(request):
    db = product.objects.filter(category="set")
    is_tr = [i % 3 == 2 for i in range(len(db))]
    dic = {"mainList": zip(is_tr, db)}
    return render(request, "KingsMan.html", dic)


def outer(request):
    db = product.objects.filter(category="outer")
    is_tr = [i % 3 == 2 for i in range(len(db))]
    dic = {"mainList": zip(is_tr, db)}
    return render(request, "template.html", dic)

def shirts(request):
    db = product.objects.filter(category="shirts")
    is_tr = [i % 3 == 2 for i in range(len(db))]
    dic = {"mainList": zip(is_tr, db)}
    return render(request, "template.html", dic)

def pants(request):
    db = product.objects.filter(category="pants")
    is_tr = [i % 3 == 2 for i in range(len(db))]
    dic = {"mainList": zip(is_tr, db)}
    return render(request, "template.html", dic)

def shoes(request):
    db = product.objects.filter(category="shoes")
    is_tr = [i % 3 == 2 for i in range(len(db))]
    dic = {"mainList": zip(is_tr, db)}
    return render(request, "template.html", dic)

def accessory(request):
    db = product.objects.filter(category="accessory")
    is_tr = [i % 3 == 2 for i in range(len(db))]
    dic = {"mainList": zip(is_tr, db)}
    return render(request, "template.html", dic)

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