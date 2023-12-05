
class Sessão:
    #Construct
    def __init__(self, sessao_Id, capacidade, horario, Id_filme, Id_sala):
        self.sessao_Id = sessao_Id
        self.capacidade = capacidade
        self.horario = horario
        self.Id_filme = Id_filme
        self.Id_sala = Id_sala

    #Gets and sets
    def getsessao_Id(self):
        return self.__sessao_Id
    def setsessao_Id(self, sessao_Id):
        self.__sessao_Id = sessao_Id
    def getCapacidade(self):
        return self.__capacidade
    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade
    def getIdfilme(self):
        return self.__Id_filme
    def setIdfilme(self, Id_filme):
        self.__Id_filme = Id_filme
    def getIdSala(self):
        return self.__Id_sala
    def setIdSala(self, Id_sala):
        self.__Id_sala = Id_sala

