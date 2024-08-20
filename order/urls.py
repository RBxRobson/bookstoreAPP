from django.urls import path, include
from rest_framework import routers

from order import viewsets

# Cria um roteador simples do Django REST Framework para gerenciar as rotas da API.
router = routers.SimpleRouter()

# Registra o ViewSet de pedidos (OrderViewSet) no roteador.
# 'order/' define o prefixo da URL para as rotas deste ViewSet.
# basename="order" é utilizado para gerar nomes de rotas únicas, 
# como 'order-list' e 'order-detail'.
router.register(r'order', viewsets.OrderViewSet, basename="order")

# Define as URLs da aplicação, incluindo as rotas 
# geradas automaticamente pelo roteador.
urlpatterns = [
    # Inclui todas as rotas do roteador na raiz ('').
    path('', include(router.urls))
]
