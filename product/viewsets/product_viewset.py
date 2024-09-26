from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


# Viewset para o modelo Product, que oferece operações CRUD automáticas.
class ProductViewSet(ModelViewSet):
    # Define as classes de Autenticação para
    # sessão, credenciais básicas, ou token.
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]

    # IsAuthenticated permite o acesso somente a usuários que estão autenticados.
    permission_classes = [IsAuthenticated]

    # Define o serializador que converte os objetos Product para JSON e vice-versa.
    serializer_class = ProductSerializer

    # Método que retorna o conjunto de dados a ser manipulado pelo ViewSet.
    # Aqui estamos sobrescrevendo o método get_queryset para personalizar o queryset.
    def get_queryset(self):
        # Retorna todos os objetos da tabela Product.
        return Product.objects.all().order_by("id")
