from django.urls import path
from .views import lojaAPIView, lojasAPIView

urlpatterns = [
    path('loja/', lojaAPIView.as_view(), name = 'loja'),
    path('loja/<int:pk>/',lojasAPIView.as_view(), name='loja')
]
