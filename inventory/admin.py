from django.contrib import admin
from .models import Autor, Genero, Idioma, Livro, Avaliacao, Estante

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Livro)
admin.site.register(Avaliacao)
admin.site.register(Estante)
