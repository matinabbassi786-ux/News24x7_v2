from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Home.views import HomePage


urlpatterns = [
    path('<user>/<id>/', HomePage, name='home')
]
