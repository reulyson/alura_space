from django.urls import path # Importa a função 'path' para definir rotas
from usuarios.views import login, cadastro

urlpatterns = [# Define uma lista de padrões de URL
    path('login', login, name='login'), # Rota para a página de login
    path('cadastro', cadastro, name='cadastro'), # Rota para a página de login
]