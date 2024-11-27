from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def friend(request):
    return HttpResponse('<h1>chaitanya is my bestfriend</h1>')
