"""
URL configuration for car1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from car2.views import *
from car3.views import *
import car4
import car4.urls
import car5
import car5.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('highend/',highend,name='highend'),
    path('byke/',byke,name='byke'),
    path('car4/',include(car4.urls)),
    path('car5/',include(car5.urls)),
]
