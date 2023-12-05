from classes.Ingresso import Ingresso
from conexão import conexao
class IngressoDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql = "SELECT * FROM Ingresso"
        cursor = c.conn.execute(sql)
        ingressos = []
        for row in cursor.fetchall():
            ingresso = Ingresso(row[0], row[1], row[2], row[3])
            ingressos.append(ingresso)
        return ingressos

    def inserir_ingresso(self,valor, Id_cliente, Id_sessao):
        c = conexao()
        sql = "INSERT INTO Ingresso(valor, Id_cliente, Id_sessao) VALUES (?,?,?)"
        cursor = c.conn.execute(sql, (valor, Id_cliente, Id_sessao))
        c.conn.commit()
        c.conn.close()
        print("ingresso inserido!")

    def deleta_ingresso(self, ID):
        c = conexao()
        sql = "DELETE FROM Ingresso WHERE Cod_ingresso = ?"
        cursor = c.conn.execute(sql, (ID,))
        c.conn.commit()
        c.conn.close()
        print("ingresso deletado!")
