from django.shortcuts import render, get_object_or_404 # Importa a função render para renderizar templates e get_object_or_404  o objeto do banco de dado pelo seu id ou gerar o código 404 (não encontrado)
from galeria.models import Fotografia

def index(request):

    fotografias = Fotografia.objects.all() # Busca todas as fotografias no banco de dados
    return render(request, 'galeria/index.html', {"cards": fotografias})  # Renderiza a página inicial com as fotografias

def imagem(request, foto_id):
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Captura a fotografia com o ID fornecido ou retorna 404 se não encontrar
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia}) # Renderiza a página da imagem com o objeto da fotografia