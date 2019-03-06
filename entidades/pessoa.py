class Pessoa():

    def __init__(self, cpf, senha):
        self.__cpf   = cpf
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf

    @property
    def senha(self):
        return  self.__senha

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @senha.setter
    def senha(self,senha):
        self.__senha = senha