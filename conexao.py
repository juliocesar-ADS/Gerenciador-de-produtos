import mysql.connector

def conectar():

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="estoque"
    )

    return conn