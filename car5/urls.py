from django.urls import path
from car5.views import *
urlpatterns=[
    path('friend/',friend,name='friend'),
]