from django.contrib import admin
from django.urls import path
from portfolioapi.views import *
 
urlpatterns = [
    path('contact',ContactFormView.as_view())
    
    ]