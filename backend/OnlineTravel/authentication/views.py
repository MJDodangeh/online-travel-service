from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
# Create your views here.

class RegisterAPI():
    def post(self, request):
        serializer = RegisterSerializer
        firstName = serializer.data["firstName"]
        lastName = serializer.data["lastName"]
        email = serializer.data["email"]
        username = serializer.data["username"]
        password = serializer.data["password"]


class LoginAPI():
    def post(selfcrequest):
        serializer = LoginSerializer
        username = serializer.data["username"]
        password = serializer.data["password"]

