class Sala:
    #Construct
    def __init__(self, cod_sala, liberado, nome_sala):
        self.cod_sala = cod_sala
        self.liberado = liberado
        self.nome_sala = nome_sala

    #GETS AND SETS
    def getCodSala(self):
        return self.cod_sala
    def setCodSala(self, cod_sala):
        self.__cod_sala = cod_sala
    def getLiberado(self):
        return self.cod_sala
    def setLiberado(self, liberado):
        self.__liberado = liberado
    def getSala(self):
        return self.nome_sala
    def setSala(self, nome_sala):
        self.__nome_sala = nome_sala 
        