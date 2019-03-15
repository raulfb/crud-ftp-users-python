from wtforms import Form
from wtforms import StringField
from wtforms import validators

# Clase para el formulario de inserccion de datos
class InsertForm(Form):
    usuario = StringField('usuario',
            [validators.Required(message = 'Introducce un usuario')
            ]
            )
    clave = StringField('clave',
            [validators.Required(message = 'Introducce una clave')
            ]
            )
# Clase para el formulario de borrado de datos
class DeleteForm(Form):
    usuario = StringField('usuario',
            [validators.Required(message = 'Introducce un usuario')
            ]
            )
