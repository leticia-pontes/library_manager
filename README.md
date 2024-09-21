# Biblioteca de Livros

Projeto pessoal de biblioteca de livros para aprendizado do framework Django.

## Descrição

Este projeto é uma aplicação de biblioteca de livros, desenvolvida para aprender e praticar o uso do Django. A aplicação permite que usuários façam login, cadastrem livros, avaliem livros e gerenciem suas listas de leitura.

## Funcionalidades

- **Cadastro e Login de Usuários**: Permite que usuários se registrem e façam login na aplicação.
- **Gerenciamento de Livros**: Usuários podem adicionar, editar e remover livros da biblioteca.
- **Avaliações**: Usuários podem avaliar livros e deixar comentários.
- **Listas de Leitura**: Os usuários podem criar e gerenciar suas listas de leitura.

## Tecnologias Utilizadas

- Python
- Django
- SQLite (banco de dados padrão)
- HTML/CSS

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/leticia-pontes/library_manager
   cd library_manager
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. Instale as dependências (ainda não definido):

   ```bash
   pip install -r requirements.txt
   ```

5. Configure o banco de dados e as variáveis de ambiente:

   - Crie um arquivo `.env` na raiz do projeto e adicione suas variáveis de ambiente (exemplo: `SECRET_KEY`, `DATABASE_URL`).

6. Realize as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

8. Acesse a aplicação em seu navegador: `http://127.0.0.1:8000/`

## Licença

Este projeto é de uso pessoal e não possui uma licença específica.
