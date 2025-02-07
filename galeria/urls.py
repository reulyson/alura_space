from django.urls import path # Importa a função 'path' para definir rotas
from galeria.views import index  # Importa a função 'index' da view
from galeria.views import imagem# Importa a função 'imagem' da view

urlpatterns = [ # Define uma lista de padrões de URL
    path('', index, name='index'), # Rota para a página inicial
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Rota para a página da imagem, recebendo o id da foto
]