from django.urls import path # Importa a função 'path' para definir rotas
from galeria.views import index  # Importa a função 'index' da view
from galeria.views import imagem# Importa a função 'imagem' da view

urlpatterns = [ # Define uma lista de padrões de URL
    path('', index, name='index'), # Rota para a URL raiz ('/'), que chama a função 'index'
    path('imagem/', imagem, name='imagem'), # Rota para a URL raiz ('imagem/'), que chama a função 'imagem'
]