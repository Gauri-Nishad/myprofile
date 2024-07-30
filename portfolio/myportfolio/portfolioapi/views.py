from django.shortcuts import render

# Create your views here.

import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .serializers import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class ContactFormView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        data=request.data
        name=request.data.get('name')
        email=request.data.get('email')
        phone=request.data.get('phone')
        usermessage=request.data.get('message')
        if not name:
            return Response({"msg":"please enter your name",'n':0})
    
        if len(str(phone)) != 10:
            return Response({'msg':'mobile number must be 10 digit','n':0})
        if not email:
            return Response({"msg":"please enter your email",'n':0})
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email) :
            return Response({'msg': 'Incorrect email id','n':0})
        if not usermessage:
            return Response({"msg":"please write message",'n':0})
        if serializer.is_valid():
            html_content = render_to_string("content.html", {'user_data': data})
            # text_content = strip_tags(html_content)
            mail= EmailMultiAlternatives(
            subject="Testing Email Message",
            body=html_content,   
            from_email="gaurinishad18@gmail.com",
            to=[email],  
            )
            mail.attach_alternative(html_content, "text/html")
            mail.send(fail_silently=False)
        
            serializer.save() 
           
            return Response({'msg':"your message has been sent",'data':serializer.data,'n':1})
        return Response({'msg':"something went wrong",'error':serializer.errors,'n':0})
