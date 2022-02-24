from django.shortcuts import render
from .models import loja
from .serializers import lojaSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class lojaAPIView(generics.ListCreateAPIView):
    queryset = loja.objects.all()
    serializer_class = lojaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nome']
    
    
class lojasAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= loja.objects.all()
    serializer_class= lojaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nome']