"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index),
    path("outer", outer, name="outer"),
    path("shirts", shirts, name="shirts"),
    path("pants", pants, name="pants"),
    path("shoes", shoes, name="shoes"),
    path("accessory", accessory, name="accessory"),
    path("search", search, name="search"),
    path("cart", cart, name="cart"),
    path("question", question, name="question"),
    path("login", login, name="login"),
    path("join", join, name="join"),
    path("game", game, name="game"),
    path("item/<int:itemnumber>", item, name="item"),
    path("banner", banner, name="banner"),
    path("loginF", loginF, name="loginF"),
    path("logoutF", logoutF, name="logoutF"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)