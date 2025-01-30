from django.shortcuts import render  # Importa a função render para renderizar templates

def index(request):
   
    return render(request, 'galeria/index.html') # Renderiza o template 'index.html'