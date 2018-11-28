from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product, productPhoto, cart
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

class cartProcess(View):
    def get(self, request):
        cartList = cart.objects.filter(userName=request.user)
        return render(request, "cart.html", {"product":cartList})

    def post(self, request):
        code = request.POST["code"]
        productNum = request.POST["amount"]
        size = request.POST["size"]
        db = product.objects.get(code=code)
        cartProduct = cart(name=db, amount=productNum, size=size, userName=request.user)
        cartProduct.save()
        return redirect("cart")


def delete(request, code):
    cartList = cart.objects.filter(userName=request.user)
    for i in cartList:
        if (i.name.code == code):
            i.delete()
            return redirect("cart")
    #return redirect("cart")
    return HttpResponse("탐색실패")

def allDelete(request):
    cartList = cart.objects.filter(userName=request.user)
    cartList.delete()
    return redirect("cart")

def change_number(request):
    userName = request.GET["userName"]
    item = request.GET["item"]
    count = request.GET["count"]
    return redirect(cart)

def question(request):
    return render(request, "question.html")

def login(request):
    return render(request, "login.html")

def join(request):
    return render(request, "join.html")

def game(request):
    return render(request, "game.html")

class item(View):
    def get(self, request, itemnumber):
        db = product.objects.get(code=itemnumber)
        photoList = productPhoto.objects.filter(code=db)
        return render(request, "item.html", {"product":db, "photoList":photoList, "mainPhoto":photoList[0]})
    def post(self, request):
        pass


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

