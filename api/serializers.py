from pyexpat import model
from rest_framework import serializers
from .models import loja, estoque

class lojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = loja
        fields = (
            'id',
            'nome',
            'descricao',
            'valor',
            'imagem',
        )

class estoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model= estoque
        fields = (
            'vendedor',
            'venda',
        )