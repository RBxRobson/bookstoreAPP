import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory


# Classe de teste para o ViewSet de Order, utilizando o APITestCase
class TestOrderViewSet(APITestCase):

    # Instância do APIClient, que é utilizada para fazer 
    # requisições simuladas durante os testes.
    client = APIClient()

    # Método de configuração inicial, executado antes de cada teste.
    def setUp(self):
        # Criação de uma categoria usando uma factory. 
        # Essas factories são úteis para gerar dados de teste.
        self.categories = CategoryFactory(title="technology")
        # Criação de um produto vinculado à categoria criada.
        self.product = ProductFactory(
            title="mouse", price=100, categories=[self.categories]
        )
        # Criação de um pedido que contém o produto criado.
        self.order = OrderFactory(product=[self.product])

    # Teste para verificar se a lista de pedidos 
    # está sendo retornada corretamente.
    def test_order(self):
        # Faz uma requisição GET para a rota "order-list", 
        # simulando a versão "v1".
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )

        # Verifica se o status da resposta é HTTP 200 (OK).
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Converte o conteúdo da resposta JSON para um dicionário.
        order_data = json.loads(response.content)
        
        # Verifica se o título do produto no pedido é igual 
        # ao título do produto criado.
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        # Verifica se o preço do produto no pedido é igual 
        # ao preço do produto criado.
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        # Verifica se o status ativo do produto no pedido é igual 
        # ao status do produto criado.
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        # Verifica se o título da categoria do produto no pedido é igual 
        # ao título da categoria criada.
        self.assertEqual(
            order_data["results"][0]["product"][0]["categories"][0]["title"],
            self.categories.title,
        )

    # Teste para criar um novo pedido.
    def test_create_order(self):
        # Cria um usuário e um produto de teste.
        user = UserFactory()
        product = ProductFactory()
        
        # Prepara os dados que serão enviados no corpo da requisição POST.
        data = json.dumps({"products_id": [product.id], "user": user.id})

        # Faz uma requisição POST para a rota "order-list" 
        # com os dados preparados, simulando a versão "v1".
        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se o status da resposta é HTTP 201 (Created).
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
