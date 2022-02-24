from rest_framework import serializers
from .models import loja

class lojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = loja
        fields = (
            'id',
            'nome',
            'descricao',
            'tipo',
            'quant',
            'valor',
            'imagem',
        )
