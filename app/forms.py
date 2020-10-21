from wtforms import Form

from wtforms import validators

from wtforms import StringField
from wtforms import FileField
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=15),
		validators.Required(message="Usuario es requerido"),
	])
	password = PasswordField('Password', [
		validators.length(min=4, max=93),
		validators.Required(message="El Password es requerido"),
	])
	#confirm_password = PasswordField('Confirm Password')
	
	
class RegisterForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=15),
		validators.Required(message='El usuario es requerido'),
	])
	
	email = EmailField('Email', [
		validators.length(min=4, max=50),
		validators.Required(message='El email es requerido'),
		validators.Email(message='Ingrese un email válido'),
	])
	
	password = PasswordField('Password', [
		validators.length(min=4, max=30),
		validators.Required(message='EL password es requerido'),
		validators.EqualTo('confirm_password', message='La contraseña no coincide'),
	])
	
	confirm_password = PasswordField('Confirma Password')


