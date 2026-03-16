from django.db import models

# Create your models here.
# https://dontpad.com/fds_2b_2026.1

import datetime
from django.utils import timezone

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200, null=False) #Não pode ficar vazio, texto obrigatório
    detalhe = models.TextField(null=False) #texto obrigatório
    tentativa = models.TextField() #texto opcional, pode ficar vazio
    data_criacao = models.DateTimeField("Criado em ") #Data de criação
    usuario = models.CharField(max_length=200, null=False, default="anônimo") #Nome do usuário

    def __str__(self): #Retorna o título da pergunta, para facilitar a identificação
        return "[" + str(self.id) + "] " + self.titulo
    
    def foi_publicado_recentemente(self): #Retorna verdadeiro se a pergunta foi criada nos últimos 24 horas
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)

    def string_detalhada(self): #Retorna uma string detalhada com todas as informações da pergunta, para facilitar a visualização
        return "id: " + str(self.id) + "; titulo: " + self.titulo + "; detalhe: " + self.detalhe + "; tentativa: " + self.tentativa + "; data criação: " + str(self.data_criacao) + "; usuario: " + self.usuario


class Resposta(models.Model): #Cada resposta está associada a uma pergunta, tem um texto, um número de votos, uma data de criação e um usuário
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE) #ForeignKey para associar a resposta a uma pergunta, se a pergunta for deletada, as respostas associadas também serão deletadas
    # Foreignt para apontar uma chave primária de outra tabela
    # on_delete=models.CASCADE para deletar as respostas associadas quando a pergunta for deletada
    texto = models.TextField(null=False) #texto obrigatório, não pode ficar vazio
    votos = models.IntegerField(default=0) #Número de votos, inicia com 0, pode ser incrementado ou decrementado pelos usuários
    data_criacao = models.DateTimeField("Criado em ") #Data de criação da resposta
    usuario = models.CharField(max_length=200, null=False, default="anônimo") #Nome do usuário que criou a resposta, texto obrigatório, não pode ficar vazio, inicia com "anônimo" por padrão


    def __str__(self): #Retorna o texto da resposta, para facilitar a identificação
        return "[" + str(self.id) + "] " + self.texto
    
    def foi_publicado_recentemente(self): #Retorna verdadeiro se a resposta foi criada nos últimos 24 horas
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)
