from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import validators


# Clase formulario de insertar usuarios
class InsertForm(Form):
    usuario = StringField('Usuario',
            [validators.Required(message = 'Completa este campo')
            ]
            )

    clave = PasswordField('Clave', [
        validators.DataRequired('Completa este campo'),
        validators.EqualTo('confirm', message='Las claves deben de coincidir')
    ])

    confirm  = PasswordField('Repita la clave')


# Clase formulario de editar contrasenha
class ModForm(Form):
    
    idusuario = StringField('idusuario')
    clave2 = PasswordField('Clave', [
        validators.DataRequired('Completa este campo'),
        validators.EqualTo('confirm2', message='Las claves deben de coincidir')
    ])

    confirm2  = PasswordField('Repita la clave')
