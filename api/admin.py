from django.contrib import admin
from .models import loja, estoque

@admin.register(loja)
class lojaAdmin(admin.ModelAdmin):
    list_display= ('nome', 'descricao', 'valor', 'imagem')
    
@admin.register(estoque)
class estoqueAdmin(admin.ModelAdmin):
    list_display=('vendedor', 'venda')