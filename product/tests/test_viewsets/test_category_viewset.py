import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory
from product.models import Category


# Classe de teste para o ViewSet de Category, utilizando o APITestCase
class CategoryViewSet(APITestCase):
    # Instância do APIClient, usada para fazer
    # requisições simuladas durante os testes
    client = APIClient()

    # Método de configuração inicial, executado antes de cada teste
    def setUp(self):
        # Cria uma categoria usando uma factory para testes
        self.categories = CategoryFactory(title="books")

    # Teste para verificar se a listagem de
    # categorias está funcionando corretamente
    def test_get_all_category(self):
        # Faz uma requisição GET para a rota "category-list",
        # simulando a versão "v1"
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        # Verifica se o status da resposta é HTTP 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Converte o conteúdo da resposta JSON para um dicionário
        category_data = json.loads(response.content)

        # # Inicia o depurador interativo
        # import pdb
        # pdb.set_trace()

        # Verifica se o título da primeira categoria retornada é igual
        # ao título da categoria criada no setup
        self.assertEqual(category_data["results"][0]["title"], self.categories.title)

    # Teste para criar uma nova categoria
    def test_create_category(self):
        # Prepara os dados que serão enviados no corpo da requisição POST
        data = json.dumps({"title": "technology"})

        # Faz uma requisição POST para a rota "category-list"
        # com os dados preparados, simulando a versão "v1"
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se o status da resposta é HTTP 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Recupera a categoria criada pelo título
        created_category = Category.objects.get(title="technology")

        # Verifica se a categoria criada possui o título correto
        self.assertEqual(created_category.title, "technology")
