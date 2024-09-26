from rest_framework import serializers

from product.models.category import Category


# Definindo um serializer para o modelo Category
class CategorySerializer(serializers.ModelSerializer):
    # Classe interna Meta para definir as configurações adicionais do serializer
    class Meta:
        # Especificando que o serializer está associado ao modelo Category
        model = Category
        # Definindo os campos que serão incluídos na serialização
        fields = [
            "title",  # Campo do título da categoria
            "slug",  # Campo do slug, geralmente usado em URLs
            "description",  # Campo da descrição da categoria
            "active",  # Campo para indicar se a categoria está ativa ou não
        ]
        extra_kwargs = {"slug": {"required": False}}
