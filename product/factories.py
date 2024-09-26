import factory

from product.models import Category, Product


# Definindo uma factory para o modelo Category
class CategoryFactory(factory.django.DjangoModelFactory):
    # Gerando um título aleatório usando o faker (com caracteres aleatórios)
    title = factory.Faker("pystr")
    # Gerando um slug aleatório
    slug = factory.Faker("pystr")
    # Gerando uma descrição aleatória
    description = factory.Faker("pystr")
    # Escolhendo aleatoriamente entre True ou False para o campo active
    active = factory.Iterator([True, False])

    # Definindo configurações adicionais para a factory
    class Meta:
        # Especificando o modelo que essa factory cria
        model = Category


# Definindo uma factory para o modelo Product
class ProductFactory(factory.django.DjangoModelFactory):
    # Gerando um preço aleatório usando o faker
    price = factory.Faker("pyint")
    # Usando LazyAttribute para gerar uma instância de
    # Category com CategoryFactory
    categories = factory.LazyAttribute(CategoryFactory)
    # Gerando um título aleatório para o produto
    title = factory.Faker("pystr")

    # Definindo configurações adicionais para a factory
    class Meta:
        # Especificando o modelo que essa factory cria
        model = Product
        skip_postgeneration_save = True

    # Método executado após a criação do produto,
    # usado para adicionar categorias ao produto
    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        # Se o objeto ainda não foi criado no banco de dados, retorna
        if not create:
            return

        # Se categorias foram passadas como argumento,
        # adiciona cada uma ao produto
        if extracted:
            for categories in extracted:
                self.categories.add(categories)
        self.save()
