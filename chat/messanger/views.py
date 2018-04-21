from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
from rest_framework.decorators import api_view

from rest_framework import generics
from messanger.serializers import MessageSerializer
from messanger.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
@csrf_exempt
def chat_list(request):
    try:
        if request.method == "GET":
            messages = Message.objects.all()
            message_json = [message.to_json() for message in messages]
            return JsonResponse(message_json, safe=False)

        elif request.method == "POST":
            data = JSONParser().parse(request)
            ser = MessageSerializer(data = data)
            if(ser.is_valid()):
              ser.save()
              return JsonResponse(ser.data, status=201)
            return JsonResponse(ser.errors, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET', 'POST'])
@csrf_exempt
def user_list(request):
    try:
        if request.method == "GET":
            users = User.objects.all()
            ser = UserSerializer(users, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)

    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def detail(request, message_id):
    try:
        message = Message.objects.get(message_id=message_id)
    except Exception as e:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        ser = MessageSerializer(message, data=data)

        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        return JsonResponse(ser.errors, status=400)
        
    elif request.method == "DELETE":
        otvet = message
        message.delete()
        return JsonResponse(otvet)


