from wtforms import Form
from wtforms import StringField
from wtforms import validators


# Clase para el formulario de inserccion de datos
class InsertForm(Form):
    usuario = StringField('usuario',
            [validators.Required(message = 'Introducce un usuario')
            ]
            )
#     clave = StringField('clave',
#             [validators.Required(message = 'Introducce una clave')
#             ]
#             )

    clave = StringField('clave', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm  = StringField('Repita la clave')

#     clave = StringField('clave',
#             [validators.Required(message = 'Introducce una clave')
#             ]
#             )