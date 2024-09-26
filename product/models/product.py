from django.db import models
from .category import Category


# Definição do modelo Product
class Product(models.Model):
    # Campo para o título do produto, obrigatório,
    # com comprimento máximo de 100 caracteres
    title = models.CharField(max_length=100)

    # Campo para a descrição do produto, opcional,
    # com comprimento máximo de 500 caracteres
    # 'blank=True' permite que o campo seja vazio no formulário,
    # e 'null=True' permite que seja NULL no banco de dados
    description = models.TextField(max_length=500, blank=True, null=True)

    # Campo para o preço do produto, que deve ser um número inteiro positivo,
    # opcional, 'null=True' permite que o campo seja NULL no banco de dados
    price = models.PositiveIntegerField(null=True)

    # Campo booleano que indica se o produto está ativo ou não,
    # padrão é True (ativo)
    active = models.BooleanField(default=True)

    # Campo ManyToMany para relacionar o produto com uma ou mais categorias
    # 'blank=True' permite que o campo seja deixado em branco no formulário
    categories = models.ManyToManyField(Category, blank=True)
