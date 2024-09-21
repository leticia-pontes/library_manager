# Generated by Django 5.1.1 on 2024-09-21 02:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('biografia', models.TextField()),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('total_paginas', models.IntegerField()),
                ('paginas_lidas', models.IntegerField(default=0)),
                ('finalizado', models.BooleanField(default=False)),
                ('ano_publicacao', models.IntegerField()),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('imagem_capa', models.ImageField(upload_to='capas/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.autor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.genero')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livros', models.ManyToManyField(to='inventory.livro')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.livro')),
            ],
        ),
    ]
