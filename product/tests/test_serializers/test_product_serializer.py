from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


# Teste unitário para o serializer ProductSerializer
class TestProductSerializer(TestCase):
    # Método de configuração inicial, executado antes de cada teste
    def setUp(self) -> None:
        # Criando uma instância de Category com o título "technology"
        self.categories = CategoryFactory(title="technology")

        # Criando uma instância de Product com título "mouse",
        # preço 100, e a categoria "technology"
        self.product_1 = ProductFactory(
            title="mouse", price=100, categories=[self.categories]
        )

        # Serializando a instância de Product para gerar os dados
        # que serão validados no teste
        self.product_serializer = ProductSerializer(self.product_1)

    # Teste principal para validar o comportamento do serializer
    def test_product_serializer(self):
        # Extraindo os dados serializados em um dicionário
        serializer_data = self.product_serializer.data

        # Verificando se o preço na serialização corresponde ao valor definido (100)
        self.assertEqual(serializer_data["price"], 100)

        # Verificando se o título na serialização
        # corresponde ao valor definido ("mouse")
        self.assertEqual(serializer_data["title"], "mouse")

        # Verificando se o título da categoria na serialização
        # corresponde ao valor definido ("technology")
        self.assertEqual(serializer_data["categories"][0]["title"], "technology")
