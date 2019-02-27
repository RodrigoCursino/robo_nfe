import os
import xml.etree.ElementTree as ET

class ReadXmls():

    ids      = []
    xml_list = []
    root     = ""

    def __init__(self, file):
        self.__file = file

    def setFile(self):
        full_file = os.path.abspath(os.path.join('data', self.__file))
        tree      = ET.parse(full_file)
        self.root      = tree.getroot()
        self.buscarId()

        #TODO passar o diretorio e ele pegar todos arquivos daquele diretório
        return self.ids[0]


    def buscarId(self):
        for child in self.root:
            if (child.tag == "infCFe"):
                id = child.attrib
                self.ids.append(id['Id'].replace('CFe',''))
