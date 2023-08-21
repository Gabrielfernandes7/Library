# Library API - Flask 📚


<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" height="18%" width="18%" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" height="20%" width="20%" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original-wordmark.svg" height="20%" width="20%"/>     
          
Este projeto é uma api desenvolvida com Flask, SQLAlchemy (SQLite3), Migrate e com template engine Jinja

## Descrição Geral

- **Cadastro de Livros:** Com esta API, você pode facilmente cadastrar informações detalhadas sobre os livros disponíveis na biblioteca, como título, autor, gênero e ISBN.

- **Cadastro de Pessoas:** Além dos livros, é possível registrar informações sobre as pessoas que utilizam a biblioteca. Isso inclui detalhes como nome, email etc.

## Bibliotecas necessária para o projeto
    Flask
    Flask-SQLAlchemy
    SQLite3

Para baixar essas bibliotecas basta executar o comando a seguir:
```bash
$ git checkout develop
$ pip install -r requirements.txt
```

## Endpoints e Methods
    index           GET        /

    books.create    GET, POST  /books/create
    books.delete    GET, POST  /books/delete/<int:id>
    books.recovery  GET        /books/recovery
    books.update    GET, POST  /books/update/<int:id>

    rent.create     GET, POST  /rents/create
    rent.delete     GET, POST  /rents/delete/<int:id>
    rent.recovery   GET        /rents/recovery
    rent.update     GET, POST  /rents/update/<int:id>

    users.create    GET, POST  /users/create
    users.delete    GET, POST  /users/delete/<int:id>
    users.recovery  GET        /users/recovery
    users.update    GET, POST  /users/update/<int:id>