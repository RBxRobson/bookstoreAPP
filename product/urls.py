from django.urls import path, include
from rest_framework import routers

from product import viewsets

# Cria um roteador simples para gerenciar as rotas da API.
router = routers.SimpleRouter()

# Registra o ViewSet de produto no roteador.
# O primeiro argumento é o prefixo da URL, ou seja, 'product/'.
# O segundo argumento é o ViewSet que será associado à rota.
# O basename define o nome base para as rotas geradas 
# (útil para construir URLs reversas).
router.register(r'product', viewsets.ProductViewSet, basename="product")

# Define as URLs da aplicação. 
# Aqui estamos incluindo todas as URLs geradas automaticamente pelo roteador.
urlpatterns = [
    # Inclui todas as rotas do roteador na raiz ('').
    path('', include(router.urls))  
]
