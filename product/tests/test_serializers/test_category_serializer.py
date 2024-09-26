from django.test import TestCase

from product.factories import CategoryFactory
from product.serializers import CategorySerializer


# Teste unitário para o serializer CategorySerializer
class TestCategorySerializer(TestCase):
    # Método de configuração inicial, executado antes de cada teste
    def setUp(self) -> None:
        # Criando uma instância de Category usando CategoryFactory com o título "food"
        self.category = CategoryFactory(title="food")

        # Serializando a instância de Category para gerar os dados
        # que serão validados no teste
        self.category_serializer = CategorySerializer(self.category)

    # Teste principal para validar o comportamento do serializer
    def test_category_serializer(self):
        # Extraindo os dados serializados em um dicionário
        serializer_data = self.category_serializer.data

        # Verificando se o título na serialização corresponde ao valor definido ("food")
        self.assertEqual(serializer_data["title"], "food")
