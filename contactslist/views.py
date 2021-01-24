from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Contact

def index(request):
    return HttpResponse('Hello World')

def display(request):
    contacts = Contact.objects.all()

    myList=""
    for myCounter in contacts:
        myList+=myCounter.to_string()+'<br>'+'<br>'
    return HttpResponse("<h1>List of Contacts</h1><br><br>"+myList)