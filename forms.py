from wtforms import Form
from wtforms import StringField
from wtforms import validators


# Clase formulario de insertar usuarios
class InsertForm(Form):
    usuario = StringField('Usuario',
            [validators.Required(message = 'Completa este campo')
            ]
            )

    clave = StringField('Clave', [
        validators.DataRequired('Completa este campo'),
        validators.EqualTo('confirm', message='Las claves deben de coincidir')
    ])

    confirm  = StringField('Repita la clave')


# Clase formulario de editar contrasenha
class ModForm(Form):
    
    idusuario = StringField('idusuario')
    clave2 = StringField('Clave', [
        validators.DataRequired('Completa este campo'),
        validators.EqualTo('confirm2', message='Las claves deben de coincidir')
    ])

    confirm2  = StringField('Repita la clave')
