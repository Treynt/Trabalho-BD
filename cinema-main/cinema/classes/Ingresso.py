class Ingresso():
    #Construct
    def __init__(self, codigoIngresso, valor, IDcliente, IDsessao):
        self.codigoIngresso = codigoIngresso
        self.valor = valor
        self.IDcliente = IDcliente
        self.IDsessao = IDsessao

    #GETS AND SETS
    def getCodigoIngresso(self):
        return self.__codigoIngresso
    def setCodigoIngresso(self, codigoIngresso):
        self.__codigoIngresso = codigoIngresso
    def getValor(self):
        return self.__valor
    def setValor(self, valor):
        self.__valor = valor
    def getIDcliente(self):
        return self.__IDcliente
    def setIDcliente(self, IDcliente):
        self.__IDcliente = IDcliente
    def getIDsessao(self):
        return self.__IDsessao
    def setIDsessao(self, IDsessao):
        self.__IDsessao = IDsessao