from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def byke(request):
    return HttpResponse('<h1>DUKE is my favourite byke</h1>')
