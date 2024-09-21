from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    biografia = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Genero(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Idioma(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    total_paginas = models.IntegerField()
    paginas_lidas = models.IntegerField(default=0)
    finalizado = models.BooleanField(default=False)
    ano_publicacao = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    nota = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    imagem_capa = models.ImageField(upload_to='capas/')

    def __str__(self):
        return self.titulo

class Avaliacao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação de {self.usuario.username} para {self.livro.titulo}'

class Estante(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro)

    def __str__(self):
        return f'Lista de Leitura de {self.usuario.username}'
