from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

# Criando ViewSet Order
class OrderViewSet(ModelViewSet):
    # Define o serializador que converte os objetos Order para JSON e vice-versa
    serializer_class = OrderSerializer
    
    # Define o conjunto de dados que será manipulado pelo ViewSet
    queryset = Order.objects.all()