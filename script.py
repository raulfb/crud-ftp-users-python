#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost",    # tu host, usualmente localhost
                     user="raul",         # tu usuario
                     passwd="raul96",  # tu password
                     db="vsftpd")        # el nombre de la base de datos

idprueba=146,
#b="Ramona"

cur = db.cursor()
#cur.execute("""INSERT INTO accounts (username, pass) VALUES (%s,%s)""",(a,b))
#cur.execute("""DELETE FROM `accounts` WHERE `accounts`.`username` = 'Ramon' AND 'accounts'.'pass' = 'Ramona'""")
#sql_Delete_query = """Delete from accounts where username = '%s')"""
#cur.execute(sql_Delete_query,a)
cur = db.cursor()
sql = """Delete from accounts where id = %s"""
#adr = ("Ramon", )

cur.execute(sql, idprueba)
