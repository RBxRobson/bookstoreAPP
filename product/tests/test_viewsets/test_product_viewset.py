import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


# Classe de teste para o ViewSet de Product, utilizando o APITestCase
class TestProductViewSet(APITestCase):
    # Instância do APIClient, utilizada para fazer requisições 
    # simuladas durante os testes
    client = APIClient()

    # Método de configuração inicial, executado antes de cada teste
    def setUp(self):
        # Cria um usuário para autenticação
        self.user = UserFactory()
        
        # Gera um token de autenticação para o usuário
        token = Token.objects.create(user=self.user)
        token.save()

        # Cria um produto usando uma factory
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    # Teste para verificar se todos os produtos são listados corretamente
    def test_get_all_product(self):
        # Recupera o token de autenticação gerado para o usuário
        token = Token.objects.get(user__username=self.user.username)
        
        # Adiciona o token nas credenciais para autenticar a requisição
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        
        # Faz uma requisição GET para a rota "product-list", 
        # simulando a versão "v1"
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"})
        )

        # Verifica se o status da resposta é HTTP 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Converte o conteúdo da resposta JSON para um dicionário
        product_data = json.loads(response.content)

        # Verifica se o título, preço e status ativo do 
        # produto correspondem aos dados criados no setup
        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    # Teste para criar um novo produto
    def test_create_product(self):
        # Recupera o token de autenticação gerado para o usuário
        token = Token.objects.get(user__username=self.user.username)
        
        # Adiciona o token nas credenciais para autenticar a requisição
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        
        # Cria uma categoria para associar ao produto
        category = CategoryFactory()
        
        # Prepara os dados que serão enviados no corpo da requisição POST
        data = json.dumps(
            {
                "title": "notebook",
                "price": 800.00,
                "categories_id": [category.id]
            }
        )

        # Faz uma requisição POST para a rota "product-list" 
        # com os dados preparados, simulando a versão "v1"
        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se o status da resposta é HTTP 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Recupera o produto criado pelo título
        created_product = Product.objects.get(title="notebook")

        # Verifica se o produto criado possui o título e preço corretos
        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)
