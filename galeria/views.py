from django.shortcuts import render  # Importa a função render para renderizar templates

def index(request):
   
    return render(request, 'index.html') # Renderiza o template 'index.html'