from classes.Filmegenero import filmeGenero
from conexão import conexao

class FilmeGeneroDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql = "SELECT * FROM filmeGenero"
        cursor = c.conn.execute(sql)
        filmeGeneros = []
        for row in cursor.fetchall():
            filmegenero = filmeGenero(row[0], row[1])
            filmeGeneros.append(filmegenero)
        return filmeGeneros

    def inserir_relacao(self, Id_filme, Id_genero):
        c = conexao()
        sql = "INSERT INTO filmeGenero(Id_filme, Id_genero) VALUES(?,?)"
        cursor = c.conn.execute(sql, (Id_filme, Id_genero))
        c.conn.commit()
        c.conn.close()
        print("relação inserida")

    def deleta_relacao(self, Id_filme, Id_genero):
        c = conexao()
        sql = "DELETE FROM filmeGenero WHERE Id_filme = ? AND Id_genero = ?"
        cursor = c.conn.execute(sql, (Id_filme, Id_genero))
        c.conn.commit()
        c.conn.close()
        print("relação deletada!")