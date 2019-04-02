from flask import Flask, render_template, flash
import forms
from forms import *
from flask import request
import MySQLdb

#Datos de conexion con la base de datos
db = MySQLdb.connect(host="localhost",
                     user="raul",
                     passwd="raul96",
                     db="vsftpd")


app = Flask(__name__)


# Vista para listar y crear usuarios
@app.route("/", methods = ['GET', 'POST'])
def borrar():
    title="Usuarios"
    datos = []
    cur = db.cursor()
    cur.execute("SELECT * FROM accounts")

    for row in cur.fetchall():
        usuario = {}
        usuario["id"] = row[0]
        usuario["name"] = row[1]
        usuario["passw"] = row[2]

        datos.append(usuario)

    ModForm = forms.ModForm(request.form)
    Insert_form = forms.InsertForm(request.form)

    if request.method == 'POST' and Insert_form.validate():
        a= Insert_form.usuario.data
        b= Insert_form.clave.data
        print("Usuario a insertar: " + a)
        print("Clave a insertar: " + b)
    
    
    if request.method == 'POST' and ModForm.validate():
        aa = ModForm.clave2.data

    return render_template("fborrado.html",title = title,form = Insert_form, form_modificar = ModForm,usuarios = datos)

# Vista para insertar usuarios
@app.route("/insertar/<a>/<b>/", methods = ['POST'])
def insertar(a,b):
    a = a,
    b = b,
    cur = db.cursor()
    cur.execute("""INSERT INTO accounts (username, pass) VALUES (%s,PASSWORD(%s))""",(a,b))

    return render_template("usuariocreado.html", a = a , b = b)

# Vista para editar la contrasenha del usuario
@app.route("/modificar/<contra>/<idusuario>/", methods = ['POST', 'GET'])
def modificar(contra,idusuario):
    
    contra = contra,
    idusuario = idusuario,
    
    cur = db.cursor()
    query="""UPDATE  accounts SET pass = PASSWORD(%s) WHERE id = %s """   
    cur.execute(query, (contra, idusuario,))

    return render_template("usuarioeditado.html", contra = contra , idusuario = idusuario)
    
# Vista oculta para borrar usuarios
@app.route("/borrar/<id>/", methods = ['POST'])
def borrar_id(id):
    id = id,
    cur = db.cursor()
    sql = """Delete from accounts where id = %s"""
    cur.execute(sql, id)
    
    return render_template("usuarioborrado.html", id = id)
    
if __name__ == "__main__":
    app.run(debug=True,port=5001)
