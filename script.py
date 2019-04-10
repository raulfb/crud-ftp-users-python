#!/usr/bin/python
  
import MySQLdb

db = MySQLdb.connect(host="localhost",    # tu host, usualmente localhost
                     user="raul",         # tu usuario
                     passwd="raul96",  # tu password
                     db="vsftpd")        # el nombre de la base de datos

contra=146,
usuario="maria"
#b="Ramona"

#cur = db.cursor()
#cur.execute("""INSERT INTO accounts (username, pass) VALUES (%s,%s)""",(a,b))
#cur.execute("""DELETE FROM `accounts` WHERE `accounts`.`username` = 'Ramon' AND 'accounts'.'pass' = 'Ramona'""")
#sql_Delete_query = """Delete from accounts where username = '%s')"""
#cur.execute(sql_Delete_query,a)
cur = db.cursor()
#sql = """Delete from accounts where id = %s"""
query="""UPDATE  accounts SET pass = PASSWORD(%s) WHERE username = %s """
cur.execute(query, (contra, usuario,))
#adr = ("Ramon", )

#cur.execute(sql, idprueba)

