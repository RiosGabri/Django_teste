# Aplicação de comandos 

#### Lembre de instalar as extensões Python + Django e SQLite Viewer para usar o código

- `py -m venv .venv` -> Criação de novo ambiente digital
- `.venv\scripts\activate` -> Ativar ambiente digital
- `pip install -r requirements.txt` -> Instalar os frameworks listados no arquivo requirements.txt
- `pip freeze` -> Listar os componentes e suas versões que foram instalados
- `pip freeze > requirements.txt` -> Retorna a saída desse comando (pip freeze) no arquivo requirements.txt
- `py -m django --version` -> Ver a versão dos instalados
- `django-admin startproject project .` -> Criar uma pasta chamada project que possui arquivos do projeto
- `py manage.py runserver` -> Inicia o servidor web
- `py manage.py startapp nome_app` -> Inicia uma nova pasta com os arquivos do projeto/app 

- `py manage.py migrate` -> Implementar os scripts criados, construção do squlite
- `py manage.py makemigrations forum` Cria os scripts/model para a base do banco de dados
- `py manage.py sqlmigrate forum 0001` -> Exibe os comandos sql da tabela 