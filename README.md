Todo List
Um aplicativo simples de lista de tarefas feito com Django.

Requisitos

Certifique-se de ter as seguintes ferramentas instaladas:
• Python (versão 3.13)
• Poetry (para gerenciamento de dependências)
• Django (instalado via Poetry)


Instalação

1. Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>

2. Instale as dependências usando o Poetry:
poetry install

3. Ative o ambiente virtual do Poetry:
poetry shell

4. Execute as migrações do banco de dados:
python manage.py migrate

5. Inicie o servidor de desenvolvimento:
python manage.py runserver



Como Usar
Acesse o aplicativo no navegador em http://127.0.0.1:8000.
Adicione, edite e remova tarefas na lista de afazeres.