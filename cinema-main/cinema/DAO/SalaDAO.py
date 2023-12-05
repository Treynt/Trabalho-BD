from classes.Sala import Sala
from conexão import conexao
class SalaDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql="SELECT * FROM Sala"
        cursor = c.conn.execute(sql)
        salas = []
        for row in cursor.fetchall():
            sala = Sala(row[0], row[1], row[2])
            salas.append(sala)
        return salas
    def inseri_sala(self, liberado, nome_sala):
        c = conexao()
        sql = "INSERT INTO Sala(Liberado, nome_sala) VALUES (?, ?)"
        cursor = c.conn.execute(sql, (liberado, nome_sala))
        c.conn.commit()
        c.conn.close()
        print("sala inserida!")
