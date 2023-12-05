class Genero():
    #Construct
    def __init__(self, IdGenero, NomeGenero):
        self.IdGenero = IdGenero
        self.NomeGenero = NomeGenero

    #GETS AND SETS
    def getIDGenero(self):
        return self.__IDGenero
    def setIDGenero(self, IDGenero):
        self.__IDGenero = IDGenero
    def getNomeGenero(self):
        return self.__NomeGenero
    def setNomeGenero(self, NomeGenero):
        self.__NomeGenero = NomeGenero