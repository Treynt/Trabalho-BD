from classes.Assento import Assento
from conexão import conexao
class AssentosDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao() 
        sql = "SELECT * FROM Assentos"
        cursor = c.conn.execute(sql)
        assentos = []
        for row in cursor.fetchall():
            assento = Assento(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21])
            assentos.append(assento)
        return assentos