class Cliente:
    def __init__(self, Id, nome, emails, senhas, sobrenomes, idades):
        self.Id = Id
        self.nome = nome
        self.emails = emails
        self.senhas = senhas
        self.sobrenomes = sobrenomes
        self.idades = idades
        

    def getId(self):
        return self.__Id
    def setId(self, Id):
        self.__Id = Id
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
    def getEmails(self):
        return self.__emails
    def setEmails(self, emails):
        self.__emails = emails
    def getSenha(self):
        return self.__senhas
    def setSenha(self, senhas):
        self.__senhas = senhas
    def getSobrenome(self):
        return self.__sobrenomes
    def setSobrenomes(self, sobrenomes):
        self.__sobrenomes = sobrenomes
    def getIdade(self):
        return self.__Idade
    def setIdade(self, idade):
        self.__idade = idade
    def getTipofuncionario(self):
        return  
    def diz_oi(self):
        print("oi")