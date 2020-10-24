import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
	
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(93), unique=True)
	email = db.Column(db.String(50), unique=True, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	
	@classmethod
	def verify_password(self, password):
    		return check_password_hash(self.encrypted_password, password)



	@property
	def password(self):
    		pass


	@password.setter
	def password(self, value):
   		self.encrypted_password = generate_password_hash(value)

	

	
	def __str__(self):
		return self.username

	@classmethod
	def createUser(cls, username, password, email):
			user = User(username=username, password=password, email=email)

			db.session.add(user)
			db.session.commit()

			return user

	@classmethod
	def get_by_username(cls, username):
    		return User.query.filter_by(username=username).first()

	@classmethod
	def get_by_id(cls, id):
    		return User.query.filter_by(id=id).first()


class Worker(db.Model):
	__tablename__ = 'workers'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	matricula = db.Column(db.String(20), nullable=False)
	turno = db.Column(db.String(50), nullable=False)
	unidad = db.Column(db.String(90), nullable=False)
	img = db.Column(db.Text, nullable=False)
	mimetype = db.Column(db.Text, nullable=False)
	img1 = db.Column(db.Text, nullable=False)
	mimetype1 = db.Column(db.Text, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())


	