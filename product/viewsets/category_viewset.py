from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


# ViewSet para o modelo Category.
class CategoryViewSet(ModelViewSet):
    # Especifica o serializer que será usado para as operações neste ViewSet.
    serializer_class = CategorySerializer

    # Define o queryset que será usado para buscar os dados.
    # Neste caso, todas as categorias serão retornadas, ordenadas pelo campo "id".
    def get_queryset(self):
        return Category.objects.all().order_by("id")
