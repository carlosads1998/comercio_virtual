from django.shortcuts import render
from .models import loja
from .serializers import lojaSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class lojaAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = loja.objects.all()
    serializer_class = lojaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nome']
    
    
class lojasAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= loja.objects.all()
    serializer_class= lojaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nome']
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer