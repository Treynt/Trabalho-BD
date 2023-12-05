
from classes.Combo import Combo
from conexão import conexao
class ComboDAO:

    def __init__(self):
        None

    def inicia(self):
        c = conexao()
        sql = 'SELECT * FROM Combo'
        cursor = c.conn.execute(sql)
        combos = []
        for row in cursor.fetchall():
            combo = Combo(row[0], row[1], row[2], row[3])
            combos.append(combo)
        return combos

    def inseri_combo(self, comidas, valor, Id_cliente):
        c = conexao()
        sql = "INSERT INTO Combo(comida, valor, Id_cliente) VALUES (?,?,?)"
        cursor = c.conn.execute(sql, (comidas, valor, Id_cliente))
        c.conn.commit()
        c.conn.close()
        print("combo inserido!")

    def deleta_combo(self, ID):
        c = conexao()
        sql = "DELETE FROM Combo WHERE Cod_comida = ?"
        cursor = c.conn.execute(sql, (ID,))
        c.conn.commit()
        c.conn.close()
        print("combo deletado!")