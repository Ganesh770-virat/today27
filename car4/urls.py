from django.urls import path
from car4.views import *
urlpatterns = [
    path('owner/',owner,name='owner'),
]