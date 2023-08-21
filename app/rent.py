from flask import Blueprint, render_template, redirect, request
from app.models.models import Rent
from database import db
from datetime import datetime

bp_rents = Blueprint(
    "rent", __name__,
    template_folder="templates/rent"
)

@bp_rents.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("rents_create.html")

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')
        date_rent = datetime.today()

    r = Rent(user_id, book_id, date_rent)

    db.session.add(r)
    db.session.commit()

    return redirect("/rents/recovery")

@bp_rents.route("/recovery")
def recovery():
    rents = Rent.query.all()

    return render_template("rents_recovery.html", rents=rents)

@bp_rents.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    r = Rent.query.get(id)

    if request.method == 'GET':
        return render_template("rents_update.html", r=r)

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')

        date_rent = datetime.today()

        db.session.add(r)
        db.session.commit()

        return redirect('/rents/recovery')

@bp_rents.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    r = Rent.query.get(id)

    if request.method == 'GET':
        return render_template("rents_delete.html", r=r)

    if request.method == 'POST':
        db.session.delete(r)
        db.session.commit()
        return redirect('/rents/recovery')
