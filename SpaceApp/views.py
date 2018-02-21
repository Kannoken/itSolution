from django.shortcuts import render
from SpaceApp.models import MsgFromSpace
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MessageSerializer

# Create your views here.
class MainPage(viewsets.ModelViewSet):
        queryset = MsgFromSpace.objects.all()
        serializer_class = MessageSerializer