from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('welcome', views.home),
    path('about', views.about),
    path('signup', views.signup),
    path('contact', views.contact),
]