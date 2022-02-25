from email.mime import image
from random import choice
from unicodedata import decimal
from click import Choice
from django.db import models


def upload_image_jogos(instance, filename):
    return f'{instance.nome}-{filename}'


class Base(models.Model):
    publicacao= models.DateTimeField(auto_now_add = True)
    atualizacao = models.DateTimeField(auto_now= True)
    
    
class loja(Base):
    
    nome =models.CharField(max_length=100)
    descricao= models.TextField(max_length=250)
    valor = models.DecimalField(decimal_places=2, max_digits=20)
    imagem = models.ImageField(upload_to=upload_image_jogos, blank=True, null=True)
    
    class Meta:
        verbose_name='jogo'
        verbose_name_plural='jogos'
    
    def __str__(self):
        return self.nome
    
class estoque(Base):
    vendedor = models.CharField(max_length=50, unique=True)
    venda = models.ForeignKey(loja, on_delete=models.CASCADE)

  
    class Meta:
        verbose_name='estoque'
        verbose_name_plural='estoques'
    
    def __str__(self):
        return f'{self.vendedor} vendeu'