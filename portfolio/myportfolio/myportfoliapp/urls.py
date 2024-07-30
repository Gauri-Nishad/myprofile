from django.contrib import admin
from django.urls import path
from myportfoliapp.views import *
 
urlpatterns = [
    
    path('base',base),
    path('',home),
    path('projects',projects,name="projects")
    
    ]