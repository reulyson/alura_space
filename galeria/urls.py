from django.urls import path # Importa a função 'path' para definir rotas
from galeria.views import index, imagem, buscar  # Importa a função da views

urlpatterns = [ # Define uma lista de padrões de URL
    path('', index, name='index'), # Rota para a página inicial
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Rota para a página da imagem, recebendo o id da foto
    path("buscar", buscar, name="buscar"), # Rota para a página buscar
]