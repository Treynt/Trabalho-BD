import sys
sys.path.append("C:\\Users\\pedro\\Desktop\\cinema")
from classes.Genero import Genero
from conexão import conexao
class GeneroDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql = "SELECT * FROM Genero"
        cursor = c.conn.execute(sql)
        generos = []
        for row in cursor.fetchall():
            genero = Genero(row[0],row[1])
            generos.append(genero)
        return generos
     
    def insere_genero(self, nome_genero):
        c = conexao()
        sql = "INSERT INTO Genero(Nome_Genero) VALUES (?)"
        cursor = c.conn.execute(sql, (nome_genero,))
        c.conn.commit()
        c.conn.close()
        print("genero inserido!")

    def deleta_genero(self, ID):
        c = conexao()
        sql = "DELETE FROM Genero WHERE ID_genero = ?"
        cursor = c.conn.execute(sql, (ID,))
        c.conn.commit()
        c.conn.close()
        print("valor deletado")

