from email.mime import image
from random import choice
from click import Choice
from django.db import models

def upload_image_jogos(instance, filename):
    return f'{instance.nome}-{filename}'


class Base(models.Model):
    publicacao= models.DateTimeField(auto_now_add = True)
    atualizacao = models.DateTimeField(auto_now= True)
    
class loja(Base):
    ST_CHOICES =(
       ( 'AÇÃO', 'AÇÃO'),
        ('ESPORTES', 'ESPORTES'),
        ('RPG', 'RPG'),
    )
    ES_CHOICES =(
        ('EM ESTOQUE', 'EM ESTOQUE'),
        ('SEM ESTOQUE', 'SEM ESTOQUE'),
    )
    nome =models.CharField(max_length=122)
    descricao= models.TextField(max_length=250)
    tipo= models.CharField(max_length=1, choices=ST_CHOICES)
    quant= models.CharField(max_length=1, choices=ES_CHOICES)
    valor = models.DecimalField(decimal_places=2, max_digits=20)
    imagem = models.ImageField(upload_to=upload_image_jogos, blank=True, null=True)
    