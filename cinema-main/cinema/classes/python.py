import sqlite3
from sqlite3 import Error
import Cliente

def ConexãoBanco():
    caminho = "BancoCinemaBD.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexãoBanco()

def inserir(conexão, sql):
    try:
        c=conexão.cursor()
        c.execute(sql)
        conexão.commit()
        print(c.fetchall())
        print("registro inserido")
    except Error as ex:
        print(ex)


