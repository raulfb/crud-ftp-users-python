from flask import Flask, render_template, flash
import forms
from flask import request
import MySQLdb

#Datos de conexion con la base de datos
db = MySQLdb.connect(host="localhost",
                     user="raul",
                     passwd="raul96",
                     db="vsftpd")


app = Flask(__name__)

# Configuracion de la pagina de inicio
@app.route("/")
def index():
    title="Home"
    return render_template("index.html",title = title)


# Pagina para probar cosas
@app.route("/pruebas/")
def pruebas():
    title="pruebas"
    return render_template("pruebas.html",title = title)


# Vista para insertar usuarios
@app.route("/insertar/", methods = ['GET', 'POST'])
def insertar():
    title="Insertar"
    Insert_form = forms.InsertForm(request.form)
    if request.method == 'POST' and Insert_form.validate():
        a= Insert_form.usuario.data
        b= Insert_form.clave.data
        print("Usuario a insertar: " + a)
        print("Clave a insertar: " + b)
        cur = db.cursor()
        cur.execute("""INSERT INTO accounts (username, pass) VALUES (%s,%s)""",(a,b))

    return render_template("finserccion.html",title = title, form = Insert_form)


# Vista para listar usuarios
@app.route("/listar/", methods = ['GET'])
def borrar():
    title="Borrar"
    datos = []
    cur = db.cursor()
    cur.execute("SELECT * FROM accounts")
    for row in cur.fetchall():
        usuario = {}
        usuario["id"] = row[0]
        usuario["name"] = row[1]
        usuario["passw"] = row[2]

        datos.append(usuario)
    
    return render_template("fborrado.html",title = title, usuarios = datos)


# Vista para borrar
@app.route("/borrar/<id>/", methods = ['POST'])
def borrar_id(id):
    id = id,
    cur = db.cursor()
    sql = """Delete from accounts where id = %s"""
    cur.execute(sql, id)

    return render_template("usuarioborrado.html", id = id)
    
if __name__ == "__main__":
    app.run(debug =True)
