"""
URL configuration for my_django_app project.

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
from django.urls import path
from kalori.views import *
urlpatterns = [

  

   
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('app/',app,name='app'),
    path('app1/',app1,name='app1'),
    path('process/', process_calories, name='process_calories'),
    path("hitung_kebutuhan_kalori", hitung_kebutuhan_kalori, name="hitung_kebutuhan_kalori"),
 




]
