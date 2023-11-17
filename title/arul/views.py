from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def offer(request):
    return render(request, 'offer.html')


def enquiry(request):
    return render(request, 'enquiry.html')


def logdata(request):
    if request.method == "POST":
        user = request.POST["Name"]
        pas = request.POST["Mobile"]

        name = Register.objects.all()
    return render(request, 'product.html')


def regdata(request):
    if request.method == "POST":
        user = request.POST["Name"]
        pas = request.POST["Mobile"]

        name = Register.objects.create(Name=user, Mobile=pas)
    return render(request, 'login.html')
    # return redirect("user_reg")


def user_reg(request):
    all_data = Register.objects.all()
    return render(request, "user_reg.html", {"key1": all_data})
