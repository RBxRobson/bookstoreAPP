from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    # Campo que exibe os detalhes dos produtos associados ao pedido
    product = ProductSerializer(read_only=True, many=True)
    
    # Campo para permitir a seleção dos produtos por ID ao criar ou atualizar
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )

    # Campo que calcula o total do pedido
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        # Calcula o total somando os preços de todos os produtos associados ao pedido
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order

        # Campos a serem exibidos na API
        fields = ["product", "total", "user", "products_id"]  

        # Torna o campo 'product' opcional
        extra_kwargs = {"product": {"required": False}}  

    def create(self, validated_data):
        # Extrai os IDs dos produtos e o usuário do payload validado
        product_data = validated_data.pop("products_id")
        user_data = validated_data.pop("user")
        
        # Cria a instância do pedido com os dados restantes, incluindo o usuário
        order = Order.objects.create(user=user_data)  

        # Associa os produtos ao pedido
        for product in product_data:
            order.product.add(product)

        return order
