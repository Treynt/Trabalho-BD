import sys
sys.path.append("C:\\Users\\pedro\\Desktop\\cinema")
from Cliente import Cliente
from conexão import conexao
class ClienteDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql = 'SELECT * FROM Cliente'
        cursor = c.conn.execute(sql)
        clientes = []
        for row in cursor.fetchall():
            cliente = Cliente(row[0], row[1], row[2], row[3], row[4], row[5])
            clientes.append(cliente)
        return clientes

    def inserir_cliente(self, nome, email, senha, sobrenome, idade):
        c = conexao()
        sql = "INSERT INTO cliente(nomes, emails, senhas, sobrenomes, idades) VALUES (?,?,?,?,?)"
        cursor = c.conn.execute(sql, (nome, email, senha, sobrenome, idade))
        c.conn.commit()
        c.conn.close()
        print("usuario inserido com sucesso!")

    def deletar_cliente(self,email):
        c = conexao()
        sql = "DELETE FROM Cliente WHERE emails = ?"
        cursor = c.conn.execute(sql, (email,))
        c.conn.commit()
        c.conn.close()
        print("cliente deletado!")

    def mudar_senha(self, nova_senha, novo_email):
        c = conexao()
        sql = "UPDATE Cliente SET senhas = ? WHERE emails = ?"
        cursor = c.conn.execute(sql,(nova_senha, novo_email))
        c.conn.commit()
        print("senha alterada!")
        
