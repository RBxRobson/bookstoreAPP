from django.db import models

# Definição do modelo Category
class Category(models.Model):
    # Campo para o título da categoria, obrigatório, 
    # com comprimento máximo de 100 caracteres
    title = models.CharField(max_length=100)
    
    # Campo para a descrição da categoria, opcional, 
    # com comprimento máximo de 200 caracteres
    # 'blank=True' permite que o campo seja vazio no formulário, 
    # e 'null=True' permite que seja NULL no banco de dados
    description = models.TextField(max_length=200, blank=True, null=True)
    
    # Campo para o slug da categoria, que deve ser único no banco de dados
    # Slugs são usados para criar URLs amigáveis 
    # com base no título da categoria
    slug = models.SlugField(unique=True)
    
    # Campo booleano que indica se a categoria está ativa ou não, 
    # padrão é True (ativa)
    active = models.BooleanField(default=True)
    
    # Método especial que retorna o título da categoria 
    # como sua representação em string
    # Útil para exibir nomes de categorias em painéis 
    # administrativos e outras interfaces
    def __unicode__(self):
        return self.title