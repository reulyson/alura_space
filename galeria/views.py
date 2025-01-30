from django.shortcuts import render  # Importa a função render para renderizar templates

def index(request):
   
    return render(request, 'galeria/index.html') #Renderiza o template 'index.html'

def imagem(request):

    return render(request, 'galeria/imagem.html') #Renderiza o template 'imagem.html'