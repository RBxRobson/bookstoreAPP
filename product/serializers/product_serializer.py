from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer


# Definindo um serializer para o modelo Product
class ProductSerializer(serializers.ModelSerializer):
    # Serializando as categorias associadas ao produto.
    # `CategorySerializer` é usado para serializar as categorias.
    # `many=True` indica que é uma lista de categorias, 
    # pois um produto pode ter múltiplas categorias.
    # `required=True` garante que o campo de categorias seja obrigatório.
    categories = CategorySerializer(required=True, many=True)

    # Classe interna Meta para definir as configurações adicionais do serializer
    class Meta:
        # Especificando que o serializer está associado ao modelo Product
        model = Product
        # Definindo os campos que serão incluídos na serialização
        fields = [
            "title",       # Campo do título do produto
            "description", # Campo da descrição do produto
            "price",       # Campo do preço do produto
            "active",      # Campo para indicar se o produto está ativo ou não
            "categories",  # Campo das categorias associadas ao produto
        ]