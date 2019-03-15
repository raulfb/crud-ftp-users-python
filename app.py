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

# Configuracion de la pagina del formulario de insertar datos
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

# Configuracion de la pagina del formulario de borrar datos
@app.route("/borrar/", methods = ['GET', 'POST'])
def borrar():
    title="Borrar"
    usuarios=[]
    contra=[]
    id=[]
    cur = db.cursor()
    cur.execute("SELECT * FROM accounts")
    for row in cur.fetchall():
        usuarios.append(row[1])
        contra.append(row[2])
        id.append(row[0])

    Delete_form = forms.DeleteForm(request.form)
    if request.method == 'POST' and Delete_form.validate():
        a= Delete_form.usuario.data,
        cur = db.cursor()
        sql = """Delete from accounts where username = %s"""
        cur.execute(sql, a)

    return render_template("fborrado.html",title = title, form = Delete_form, usuarios = usuarios, contra = contra, id = id)

# Pagina que muestra los usuarios activos
@app.route("/listar/")
def listar():
    title="Listar"
    usuarios=[]
    contra=[]
    id=[]
    cur = db.cursor()
    cur.execute("SELECT * FROM accounts")
    for row in cur.fetchall():
        usuarios.append(row[1])
        contra.append(row[2])
        id.append(row[0])

    return render_template("listar.html",title = title, usuarios = usuarios, contra = contra, id = id)

if __name__ == "__main__":
    app.run(debug =True)
