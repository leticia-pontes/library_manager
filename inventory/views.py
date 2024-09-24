from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Autor, Genero, Idioma, Livro, Avaliacao, Estante
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


## Views de Acesso

class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class AcessoLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


## Views dos Models

# Views para Autor
class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor_detail.html'

class AutorListView(CreateView):
    model = Autor
    template_name = 'autor_form.html'
    fields = ['nome', 'biografia', 'data_nascimento']

class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'autor_list.html'
    fields = ['nome', 'biografia', 'data_nascimento']

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor_confirm_delete.html'
    success_url = '/autores/'


# Views para Genero
class GeneroListView(ListView):
    model = Genero
    template_name = 'genero_list.html'

class GeneroDetailView(DetailView):
    model = Genero
    template_name = 'genero_detail.html'

class GeneroCreateView(CreateView):
    model = Genero
    template_name = 'genero_form.html'
    fields = ['descricao']
    success_url = reverse_lazy('genero_list')

class GeneroUpdateView(UpdateView):
    model = Genero
    template_name = 'genero_form.html'
    fields = ['descricao']
    success_url = reverse_lazy('genero_list')

class GeneroDeleteView(DeleteView):
    model = Genero
    template_name = 'genero_confirm_delete.html'
    success_url = reverse_lazy('genero_list')


# Views para Idioma
class IdiomaListView(ListView):
    model = Idioma
    template_name = 'idioma_list.html'

class IdiomaDetailView(DetailView):
    model = Idioma
    template_name = 'idioma_detail.html'

class IdiomaCreateView(CreateView):
    model = Idioma
    template_name = 'idioma_form.html'
    fields = ['descricao']
    success_url = reverse_lazy('idioma_list')

class IdiomaUpdateView(UpdateView):
    model = Idioma
    template_name = 'idioma_form.html'
    fields = ['descricao']
    success_url = reverse_lazy('idioma_list')

class IdiomaDeleteView(DeleteView):
    model = Idioma
    template_name = 'idioma_confirm_delete.html'
    success_url = reverse_lazy('idioma_list')


# Views para Livro
class LivroListView(ListView):
    model = Livro
    template_name = 'livro_list.html'

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livro_detail.html'

class LivroCreateView(CreateView):
    model = Livro
    template_name = 'livro_form.html'
    fields = ['titulo', 'autor', 'total_paginas', 'paginas_lidas', 'finalizado', 'ano_publicacao', 'genero', 'nota', 'isbn', 'idioma', 'imagem_capa']
    success_url = reverse_lazy('livro_list')

class LivroUpdateView(UpdateView):
    model = Livro
    template_name = 'livro_form.html'
    fields = ['titulo', 'autor', 'total_paginas', 'paginas_lidas', 'finalizado', 'ano_publicacao', 'genero', 'nota', 'isbn', 'idioma', 'imagem_capa']
    success_url = reverse_lazy('livro_list')

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('livro_list')


# Views para Avaliacao
class AvaliacaoListView(ListView):
    model = Avaliacao
    template_name = 'avaliacao_list.html'

class AvaliacaoDetailView(DetailView):
    model = Avaliacao
    template_name = 'avaliacao_detail.html'

class AvaliacaoCreateView(CreateView):
    model = Avaliacao
    template_name = 'avaliacao_form.html'
    fields = ['livro', 'usuario', 'nota', 'comentario']
    success_url = reverse_lazy('avaliacao_list')

class AvaliacaoUpdateView(UpdateView):
    model = Avaliacao
    template_name = 'avaliacao_form.html'
    fields = ['livro', 'usuario', 'nota', 'comentario']
    success_url = reverse_lazy('avaliacao_list')

class AvaliacaoDeleteView(DeleteView):
    model = Avaliacao
    template_name = 'avaliacao_confirm_delete.html'
    success_url = reverse_lazy('avaliacao_list')


# Views para Estante
class EstanteListView(ListView):
    model = Estante
    template_name = 'estante_list.html'

class EstanteDetailView(DetailView):
    model = Estante
    template_name = 'estante_detail.html'

class EstanteCreateView(CreateView):
    model = Estante
    template_name = 'estante_form.html'
    fields = ['usuario', 'livros']
    success_url = reverse_lazy('estante_list')

class EstanteUpdateView(UpdateView):
    model = Estante
    template_name = 'estante_form.html'
    fields = ['usuario', 'livros']
    success_url = reverse_lazy('estante_list')

class EstanteDeleteView(DeleteView):
    model = Estante
    template_name = 'estante_confirm_delete.html'
    success_url = reverse_lazy('estante_list')