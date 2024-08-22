from rest_framework import serializers

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    # Campo que exibe os detalhes completos das categorias associadas ao produto.
    # Este campo é somente leitura e permite múltiplas categorias.
    categories = CategorySerializer(read_only=True, many=True)
    
    # Campo que permite a seleção de categorias por seus IDs 
    # ao criar ou atualizar o produto.
    # Este campo é somente para escrita (write_only) e permite múltiplas categorias.
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        # Campos que serão expostos pela API.
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "categories",  # Detalhes completos das categorias.
            "categories_id",  # IDs das categorias para criação/atualização.
        ]

    def create(self, validated_data):
        # Extrai os IDs das categorias do payload validado.
        category_data = validated_data.pop("categories_id")

        # Cria a instância do produto com os dados restantes.
        product = Product.objects.create(**validated_data)
        
        # Adiciona cada categoria associada ao produto.
        for category in category_data:
            product.categories.add(category)

        return product
