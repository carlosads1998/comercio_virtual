from django.contrib import admin
from .models import loja

@admin.register(loja)
class lojaAdmin(admin.ModelAdmin):
    list_display= ('nome', 'descricao', 'valor', 'imagem')