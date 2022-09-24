from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, "generator/home.html",)

def password(request):



    char = list('abcdefghijklmnopstuvwyx')



    lengt = int(request.GET.get('legth',12))
    if request.GET.get("uppercase"):
        char.extend(list("AZERTYUIOPQSDFGHJKLMWXCVBN"))
    thepassword = ''
    if request.GET.get('special'):
        char.extend("&é"'(§è!çà)-=+~<>\²³µù%£´*-§#@é'"")
    if request.GET.get('numbers'):
        char.extend("1234567890")
    for i in range(lengt):
        thepassword += random.choice(char)

    return render(request, "generator/password.html", {"password": thepassword} )

def about(request):
    return  render(request, 'generator/about.html', {"j":'hello i am thomas'})
