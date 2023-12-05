import sys
sys.path.append("C:\\Users\\pedro\\Desktop\\cinema")
from conexão import conexao
from classes.Sessão import Sessão

class SessaoDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql = "SELECT * FROM Sessao"
        cursor = c.conn.execute(sql)
        sessoes = []
        for row in cursor.fetchall():
            sessao = Sessão(row[0], row[1], row[2], row[3], row[4])
            sessoes.append(sessao)
        return sessoes

    def inserir_sessao(self, capacidade, horario, Id_filme, Id_sala):
        c = conexao()
        sql = "INSERT INTO Sessao (Capacidade, Horario, Id_filme, Id_sala) VALUES (?,?,?,?)"
        cursor = c.conn.execute(sql, (capacidade, horario, Id_filme, Id_sala))
        c.conn.commit()
        c.conn.close()
        print("sessão inserida!")

    def deletar_sessao(self, ID):
        c = conexao()
        sql = "DELETE FROM Sessao WHERE Filme_Id = ?"
        cursor = c.conn.execute(sql, (ID,))
        c.conn.commit()
        c.conn.close()
        print("sessão deletada!")
    
    def alterar_capacidade(self, capacidade, ID):
        c = conexao()
        sql = "UPDATE Sessao SET Capacidade = ? WHERE Filme_ID = ?"
        cursor = c.conn.execute(sql,(capacidade, ID,))
        c.conn.commit()
        c.conn.close()