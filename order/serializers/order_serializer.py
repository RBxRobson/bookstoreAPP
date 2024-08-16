from rest_framework import serializers

from order.models import Order
from product.serializers.product_serializer import ProductSerializer

# Definindo um serializer para o modelo Order
class OrderSerializer(serializers.ModelSerializer):
    # Serializando os produtos associados ao pedido. 
    # `ProductSerializer` é usado para serializar os produtos. 
    # `many=True` indica que é uma lista de produtos, não um único produto.
    # `required=True` garante que o campo seja obrigatório.
    product = ProductSerializer(required=True, many=True)
    
    # Definindo um campo que será preenchido usando um método customizado.
    total = serializers.SerializerMethodField()

    # Método para calcular o total do pedido, 
    # somando o preço de todos os produtos.
    # `get_total` é um nome padrão usado pelo DRF 
    # para campos criados com `SerializerMethodField`.
    # O `instance` é a instância atual de Order sendo serializada.
    def get_total(self, instance):
        # Calcula o total somando o preço de cada produto.
        # `instance.product.all()` retorna todos os produtos relacionados ao pedido.
        total = sum([product.price for product in instance.product.all()])
        return total

    # Definindo configurações adicionais para o serializer
    class Meta:
        # Definindo o modelo base como Product
        model = Order
        # Especificando os campos a serem incluídos na serialização
        fields = ["product", "total"]