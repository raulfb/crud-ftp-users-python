from wtforms import Form
from wtforms import StringField
from wtforms import validators


# Clase formulario de inserccion de datos
class InsertForm(Form):
    usuario = StringField('usuario',
            [validators.Required(message = 'Completa este campo')
            ]
            )

    clave = StringField('clave', [
        validators.DataRequired('Completa este campo'),
        validators.EqualTo('confirm', message='Las claves deben de coincidir')
    ])

    confirm  = StringField('Repita la clave')
