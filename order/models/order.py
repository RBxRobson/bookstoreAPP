from django.db import models
from django.contrib.auth.models import User

# Importa o modelo Product de outro módulo
from product.models.product import Product

# Definição do modelo Order
class Order(models.Model):
    # Campo ManyToMany para associar múltiplos produtos a uma única ordem
    # 'blank=False' indica que este campo é obrigatório
    product = models.ManyToManyField(Product, blank=False)
    
    # Campo ForeignKey para associar a ordem a um usuário específico
    # 'null=False' indica que este campo é obrigatório 
    # e não pode ser NULL no banco de dados
    user = models.ForeignKey(User, on_delete=models.CASCADE)
