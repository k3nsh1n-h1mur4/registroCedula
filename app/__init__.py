from flask import Flask

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager


app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

from .views import page
from .models import User

def create_app(config):
    app.config.from_object(config)
    
    bootstrap.init_app(app)
    
    csrf.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = '.login'
    
    app.register_blueprint(page)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        
    
    return app

