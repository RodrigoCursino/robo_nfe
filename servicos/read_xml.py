import os
import xml.etree.ElementTree as ET
from entidades.xml import XML
from repositorio.xml_repositorio import XmlRepositorio

class ReadXmls():

    root     = ""

    def __init__(self, file):
        self.__file = file

    def loadFiles(self):
        full_file = os.path.abspath(os.path.join('data', self.__file))
        tree      = ET.parse(full_file)
        self.root      = tree.getroot()
        return self.load()


    def load(self):

        for child in self.root:
          if (child.tag == "infCFe"):
              id = child.attrib
              xml_id = id['Id'].replace('CFe', '')
              # PAI
              for pai in child:

                  #PAI
                  for filho in pai:
                      #Filho

                      # salvando variaveis
                      if pai.tag == 'ide' and filho.tag == 'dEmi':
                          data =  filho.text
                          data =  data[:4] + "-" + data[4:-2] + "-" + data[6:]
                      if pai.tag == 'emit' and filho.tag == 'CNPJ':
                          cnpj =  filho.text
                      if pai.tag == 'emit' and filho.tag == 'xFant':
                          nome_fantasia = filho.text
                      if pai.tag == 'dest' and filho.tag == 'CPF':
                          cpf =  filho.text
                      if pai.tag == 'total' and filho.tag == 'vCFe':
                          valor = float(filho.text)



        if cpf != None:
            #if XmlRepositorio.select_xml_by_cod(xml_id):
                return XML(xml_id, valor, data, cnpj, nome_fantasia)
                #XmlRepositorio.inserir(xml)
