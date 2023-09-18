# SpotNews

Aplicação feita no curso da Trybe do backend e frontend de um site de notícias, usando o framework **Django**, que mostra as notícias de um banco de dados **MySQL** dockerizado feito pela Trybe, com a possibilidade de criar novas notícias e categorias.

## Pastas trabalhados
[/news](https://github.com/thiagopicorelli/spotnews/tree/main/news)
[/news_rest](https://github.com/thiagopicorelli/spotnews/tree/main/news_rest)
[/spotnews](https://github.com/thiagopicorelli/spotnews/tree/main/spotnews)

## Setup
Utiliza Python 3.10.12 e Docker.

`python3 -m venv .venv && source .venv/bin/activate` para criar o ambiente virtual do projeto.

`python3 -m pip install -r dev-requirements.txt` para instalar.

`docker build -t spotnews-db .` para iniciar o docker do banco de dados.

`docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db` para setar a variáveis de sistema no docker;

`python3 manage.py migrate && python3 manage.py runscript seeds` para criar as migrations e popular o banco de dados.

`python manage.py runserver` para iniciar o frontend e backend.

`localhost:8000` é a rota padrão.

## Linguagens e Frameworks
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)