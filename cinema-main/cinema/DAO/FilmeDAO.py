import sys
sys.path.append("C:\\Users\\pedro\\Desktop\\cinema")
from classes.Filme import Filme
from conexão import conexao

class FilmeDAO:

    def __init__(self):
        None

    def inicia(self):
        c= conexao()
        sql = "SELECT * FROM Filme"
        cursor = c.conn.execute(sql)
        filmes = []
        for row in cursor.fetchall():
            filme = Filme(row[0], row[1], row[2])
            filmes.append(filme)
        return filmes

    def inserir_filme(self, titulo, classificação):
        c = conexao()
        sql = "INSERT INTO Filme(Titulo, Classificacao) VALUES (?,?)"
        cursor = c.conn.execute(sql, (titulo, classificação))
        c.conn.commit()
        c.conn.close()
        print("filme inserido!")

    def retirar_filme(self, ID):
        c = conexao()
        sql = "DELETE FROM Filme WHERE Cod_Filme = ?"
        cursor = c.conn.execute(sql, (ID,))
        c.conn.commit()
        c.conn.close()
        print("filme deletado!")
