from django.urls import path

from api.models import estoque
from .views import lojaAPIView, lojasAPIView, estoqueAPIView, estoquesAPIView

urlpatterns = [
    path('loja/', lojaAPIView.as_view(), name = 'loja'),
    path('loja/<int:pk>/',lojasAPIView.as_view(), name='loja'),
    path('estoque/<int:pk/', estoquesAPIView.as_view(), name= 'Vendas e estoque'),
    path('estoque/', estoqueAPIView.as_view(), name= 'estoque e vendas')
]
