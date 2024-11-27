from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def highend(request):
    return HttpResponse('<h1>the car is RANGEROVER</h1>')
