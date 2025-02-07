from django.db import models

class Fotografia(models.Model): # Estamos criando uma nova classe chamada Fotografia que herda de models.Model
    # adicionando campos ao modelo.
    nome = models.CharField(max_length=100, null=False, blank=False) #  Usamos CharField porque queremos armazenar uma string
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False) # usando TextField por que podemos ter textos longos
    foto = models.CharField(max_length=150, null=False, blank=False) # null=False significa que esse campo não pode ser nulo , e blank=False significa que não pode ser deixado em branco em formulários.

def __str__(self):
    return f"Fotografia [nome={self.nome}]" # Este método define como o objeto Fotografia será representado como uma string. Isso é útil para facilitar a visualização dos objetos no Django Admin ou em outros lugares.0