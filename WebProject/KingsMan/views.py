from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product, productPhoto
from django.contrib.auth.models import User
from django.contrib.auth import login as Login, logout, authenticate
from django.views import View

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

def item(request, itemnumber):
    db = product.objects.get(code=itemnumber)
    photoList = productPhoto.objects.filter(code=db)
    return render(request, "item.html", {"product":db, "photoList":photoList, "mainPhoto":photoList[0]})

def loginF(request):
    id = request.POST["id"]
    password = request.POST["password"]
    user = authenticate(request, username=id, password=password)
    if(user==None):
        return HttpResponse("정보가 없습니다.")
    Login(request, user)
    return redirect(index)

def logoutF(request):
    logout(request)
    return redirect(index)

class Join(View) :
    def get(self, request):
        return render(request, "join.html")
    def post(self, request):
        id = request.POST["id"]
        password = request.POST["password"]
        email = request.POST["email"]
        pw_confirm = request.POST["pw_confirm"]
        if (len(password) < 8):
            return HttpResponse("비밀번호를 8자 이상으로 설정해주세요.")
        if(password != pw_confirm):
            return HttpResponse("비밀번호가 일치하지 않습니다.")
        user = User.objects.create_user(id, email, password)
        user.save()
        return redirect(index)
