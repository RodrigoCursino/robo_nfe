class XML():

    def __init__(self, cod_xml, valor, data, cnpj, nome_fantasia):
        self.__cod_xml        = cod_xml
        self.__valor          = valor
        self.__data           = data
        self.__cnpj           = cnpj
        self.__nome_fantasia  = nome_fantasia


    @property
    def cod_xml(self):
       return self.__cod_xml

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @cod_xml.setter
    def cod_xml(self, cod_xml):
        self.__cod_xml = cod_xml

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @data.setter
    def data(self, data):
        self.__data = data

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia