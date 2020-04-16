"""Bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from myBakery import views as user_views

urlpatterns = [
    path('', user_views.index, name="home"),
    path('about/', user_views.about, name="about"),
    path('prodView/<int:myid>', user_views.prodView, name="prodView"),
    path('contact/', user_views.contact, name="contact"),
    path('tracker/', user_views.tracker, name="tracker"),
    path('checkout/', user_views.checkout, name="checkout"),
    path('birthday/', user_views.birthday, name="birthday"),
    path('wedding/', user_views.wedding, name="wedding")
]
