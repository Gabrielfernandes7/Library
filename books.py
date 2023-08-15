from flask import Blueprint, render_template, redirect, request
from models.models import Book
from database import db

bp_books = Blueprint(
    "books", __name__,
    template_folder="templates/books"
)

@bp_books.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("books_create.html")

    if request.method == 'POST':
        title = request.form.get('title')

    b = Books(title)

    db.session.add(b)
    db.session.commit()

    return redirect("/books/recovery")

@bp_books.route("/recovery")
def recovery():
    books = Book.query.all()

    return render_template("books_recovery.html", books=books)

@bp_books.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    b = Book.query.get(id)

    if request.method == 'GET':
        return render_template("books_update.html", b=b)

    if request.method == 'POST':
        title = request.form.get('title')

        b.title = title

        db.session.add(b)
        db.session.commit()

        return redirect('/books/recovery')

@bp_books.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    b = Book.query.get(id)

    if request.method == 'GET':
        return render_template("books_delete.html", b=b)

    if request.method == 'POST':
        db.session.delete(b)
        db.session.commit()
        return redirect('/books/recovery')
    