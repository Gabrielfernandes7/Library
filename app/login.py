from flask import Blueprint, flash, render_template, redirect
from flask_login import login_user, logout_user, login_required
from database import db
from app.models.models import User
from app.models.forms import LoginForm, RegisterForm

bp_auth = Blueprint(
    'auth', __name__,
    template_folder="templates/auth"
)

@lm.user_loader
def load_user(id_):
  return User.query.filter_by(id_=id_).first()

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect('/rents/create')
        else:
            flash('Nome ou senha de usuário incorreto')
    
    return render_template('login_form.html', form=form)

@bp_auth.route('/logout')
@login_required
def logout():
    load_user()
    return redirect('/')

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    name = form.name.data
    email = form.email.data
    password = form.password.data
    user = User(password, name, email)
    try:
      db.session.add(user)
      db.session.commit()
    except:
      flash('Usuário ou email já estão cadastrados')
    return redirect('/login')
  return render_template('register/index.html', form=form)