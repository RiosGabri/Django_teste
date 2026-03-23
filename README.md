# Aplicação de comandos 

## Lembre de instalar as extensões Python + Django e SQLite Viewer para usar o código

- `py -m venv .venv` -> Criação de novo ambiente digital
- `.venv\scripts\activate` -> Ativar ambiente digital
- `pip install -r requirements.txt` -> Instalar os frameworks listados no arquivo requirements.txt
- `pip freeze` -> Listar os componentes e suas versões que foram instalados
- `pip freeze > requirements.txt` -> Retorna a saída desse comando (pip freeze) no arquivo requirements.txt
- `py -m django --version` -> Ver a versão dos instalados
- `django-admin startproject project .` -> Criar uma pasta chamada project que possui arquivos do projeto
- `py manage.py runserver` -> Inicia o servidor web
- `py manage.py startapp nome_app` -> Inicia uma nova pasta com os arquivos do projeto/app.

## Migrate

- `py manage.py migrate` -> Implementar os scripts criados, construção do squlite
- `py manage.py makemigrations forum` Cria os scripts/model para a base do banco de dados
- `py manage.py sqlmigrate forum 0001` -> Exibe os comandos sql da tabela .

### Shell

- `py manage.py shell` -> Abre um terminal/shell do django
- `from forum.models import Pergunta, Resposta` -> Importa os models Perguntas & Resposta para o shell
- `Perguntas.objects.all()` -> Listar as perguntas criadas + Caso adicione .values() no final ele exibe todas as perguntas + Se adicionar .filter(id=1) ele exibe apenas a pergunta com id 1
- `from django.utils import timezone` -> Importa o tempo
- `q = Pergunta(titulo = "", detalhe="", tentativa="", data_criacao=timezone.now))` -> Criação da primeira pergunta + configuração da hora de criação como aquele exato instante
- `q.save()` - > Salva a pergunta
- `q.id` - > Retorna o id da pergunta (Id é gerado automaticamente ao salvar)
- `q.tentativa` -> Alterar um atributo (faz o  all().filter(id=1) e coloque q.atributo e mude, depois salve)
- `q.resposta_set.all()` -> Busca as respostas para cada pergunta/ ve quantas respostas tem cada pergunta
- `al = Resposta(pergunta=q, texto="", data...)` -> Criação de resposta
- `al.save()` -> Salvar a resposta 
- `al.delete()` -> Deletar a resposta
- `al.pergunta` -> mostra a pergunta dessa resposta
- `a3 = q.resposta_set.create(texto="", data....)` -> Cria a resposta a partir do objeto pergunta
- `quit()` -> sai do shell.

#### Admin

- `py manage.py createsuperuser` -> Cria um user/admin.