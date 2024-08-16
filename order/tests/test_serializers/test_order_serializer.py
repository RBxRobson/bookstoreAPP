from django.test import TestCase

from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers import OrderSerializer


# Teste unitário para o serializer OrderSerializer
class TestOrderSerializer(TestCase):
    # Método de configuração inicial, executado antes de cada teste
    def setUp(self) -> None:
        # Criando duas instâncias de Product usando ProductFactory
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        # Criando uma instância de Order com os produtos criados acima
        self.order = OrderFactory(product=(self.product_1, self.product_2))
        
        # Serializando a instância de Order para gerar os dados que serão validados no teste
        self.order_serializer = OrderSerializer(self.order)

    # Teste principal para validar o comportamento do serializer
    def test_order_serializer(self):
        # Extraindo os dados serializados em um dicionário
        serializer_data = self.order_serializer.data
        
        # Verificando se o título do primeiro produto no serializer corresponde ao título do produto original
        self.assertEqual(
            serializer_data["product"][0]["title"], self.product_1.title
        )
        
        # Verificando se o título do segundo produto no serializer corresponde ao título do produto original
        self.assertEqual(
            serializer_data["product"][1]["title"], self.product_2.title
        )
