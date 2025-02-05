from django.shortcuts import render  # Importa a função render para renderizar templates

def index(request):

    # criando um dicionario com informaçãoes para os cards do index
    dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org / NASA / James Webb"},
    2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}
}
   
    return render(request, 'galeria/index.html', {"cards": dados}) #Renderiza o template 'index.html' e carrega as informações do dicionário 'dados'

def imagem(request):

    return render(request, 'galeria/imagem.html') #Renderiza o template 'imagem.html'