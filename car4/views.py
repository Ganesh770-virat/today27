from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def owner(request):
    return HttpResponse('<h1>owner of my pg is pratap</h1>')
