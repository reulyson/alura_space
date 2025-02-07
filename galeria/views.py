from django.shortcuts import render, get_object_or_404 # Importa a função render para renderizar templates
from galeria.models import Fotografia

def index(request):

    fotografias = Fotografia.objects.all() # variavel criada para exibir os objetos referentes do banco de dados

    return render(request, 'galeria/index.html', {"cards": fotografias}) #Renderiza o template 'index.html' e carrega as informações do banco de dados refrentes as fotos

def imagem(request, foto_id):
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Captura a fotografia com o ID fornecido ou retorna 404 se não encontrar
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia}) # Renderiza a página da imagem com o objeto da fotografia