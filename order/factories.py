import factory
from django.contrib.auth.models import User

from order.models import Order


# Definindo uma factory para o modelo User
class UserFactory(factory.django.DjangoModelFactory):
    # Gerando um email aleatório usando o faker
    email = factory.Faker("pystr")
    # Gerando um nome de usuário aleatório usando o faker
    username = factory.Faker("pystr")

    # Definindo configurações adicionais para a factory
    class Meta:
        # Especificando o modelo que essa factory cria
        model = User


# Definindo uma factory para o modelo Order
class OrderFactory(factory.django.DjangoModelFactory):
    # Associando a factory de User à Order através do campo user
    user = factory.SubFactory(UserFactory)

    # Definindo configurações adicionais para a factory
    class Meta:
        # Especificando o modelo que essa factory cria
        model = Order
        skip_postgeneration_save = True

    # Método executado após a criação do pedido, usado para adicionar produtos ao pedido
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        # Se o pedido ainda não foi criado no banco de dados, retorna
        if not create:
            return

        # Se produtos foram passados como argumento, adiciona cada um ao pedido
        if extracted:
            for product in extracted:
                self.product.add(product)
        self.save()
