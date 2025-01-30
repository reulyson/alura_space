from django.urls import path # Importa a função 'path' para definir rotas
from galeria.views import index  # Importa a função 'index' da view

urlpatterns = [ # Define uma lista de padrões de URL
    path('', index), # Rota para a URL raiz ('/'), que chama a função 'index'
]