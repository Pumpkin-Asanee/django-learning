from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request , 'home/home.html')


def Login(request):
    return render(request , "home/login.html")

