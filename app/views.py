from flask import request, render_template, redirect, url_for, flash
from flask import Blueprint

from werkzeug.utils import secure_filename

from . import db
import os
from . import app
app.config['IMAGE_UPLOADS'] = '/Users/k3nsh1n/Pictures'

UPLOAD_FOLDER = '/Users/k3nsh1n/' 

from flask_login import current_user, login_user, logout_user, login_required

from .forms import LoginForm, RegisterForm
from .models import User, Worker

from . import login_manager

page = Blueprint('page', __name__)

@login_manager.user_loader
def loader_user(id):
    return User.get_by_id(id)



@page.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        unidad = request.form['unidad']
        if os.path.exists(request.form['unidad']):
            #print(os.path.abspath(UPLOAD_FOLDER)) return /Users/k3nsh1n
            print('Ya existe el directorio')
        else:
            os.mkdir(request.form['unidad'])
            return redirect(url_for('.registerC'))
            if os.path.exists('HGR 46'):
                print('Se creo satisfactoriamente')
    return render_template('viewMain/getUnidad.html', title='Index')
    
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
    

@page.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.register'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Usuario logueado exitosamente')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña inválidos')
            return redirect(url_for('.register'))
        return render_template('auth/login.html', title='logueate', form=form)
    return render_template('auth/login.html', title='login', form=form)
        
        
@page.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.createUser(form.username.data, form.password.data, form.email.data)
            #return redirect(url_for('.'))
            if user:
                print('Registro realizado')
    return render_template('auth/register.html', title='Registro de Usuarios', form=form)


@page.route('/ced/worker', methods=['GET', 'POST'])
def registerC():
    if request.method == 'POST':
        name = request.form['name']
        matricula = request.form['matricula']
        turno = request.form['turno']
        unidad = request.form['unidad']
        if 'file' not in request.files:
            flash('No hay archivo')
        img = request.files['img']
        img1 = request.files['img1']
        if img.filename and img1.filename == '':
            flash('No hay nombre de archivo')
        print(img.filename)
        print(img1.filename)
        filename = secure_filename(img.filename)
        filename1 = secure_filename(img1.filename)
        mimetype = img.mimetype
        mimetype1 = img1.mimetype
        
        img.save(os.path.join(app.config['IMAGE_UPLOADS'], img.filename))
        img.save(os.path.join(app.config['IMAGE_UPLOADS'], img1.filename))
        worker = Worker(name=name, matricula=matricula, turno=turno, unidad=unidad, img=img, mimetype=mimetype, img1=img1, mimetype1=mimetype1)
        db.session.add(worker)
        db.session.commit()
        if worker:
            return redirect(url_for('.list'))     
    return render_template('worker/register.html', title='Registro Cédula')


@page.route('/ced/listar', methods=['GET', 'POST'])
def list():
    if request.method == 'GET':
        worker = Worker.query.all()
    return render_template('worker/list.html', title='Listado General', worker=worker)
        
