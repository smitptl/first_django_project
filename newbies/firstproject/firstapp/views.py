from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #dict = {'name': "This is my view file"}
    return render(request, 'index.html')

def signup(request):
    return HttpResponse("please create your account!")

def contact(request):
    return HttpResponse("This is our contact details.")

def about(request):
    return HttpResponse("This is about our website")