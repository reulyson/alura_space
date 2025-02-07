from django.shortcuts import render  # Importa a função render para renderizar templates
from galeria.models import Fotografia

def index(request):

    fotografias = Fotografia.objects.all() # variavel criada para exibir os objetos referentes do banco de dados

    return render(request, 'galeria/index.html', {"cards": fotografias}) #Renderiza o template 'index.html' e carrega as informações do banco de dados refrentes as fotos

def imagem(request):

    return render(request, 'galeria/imagem.html') #Renderiza o template 'imagem.html'