import os
import xml.etree.ElementTree as ET
from entidades.xml import XML
from repositorio.xml_repositorio import XmlRepositorio

class ReadXmls():

    xml_list = []
    root     = ""

    def __init__(self, file):
        self.__file = file

    def setFile(self):
        full_file = os.path.abspath(os.path.join('data', self.__file))
        tree      = ET.parse(full_file)
        self.root      = tree.getroot()
        self.buscarId()


    def buscarId(self):

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

                          print(f"FILHO: {filho.tag} : Valor {filho.text}")
                      for neto in filho:
                          print(f"NETO: {neto.tag} = Valor {neto.text}")


        if cpf != None:
            if XmlRepositorio.select_xml_by_cod(xml_id):
                xml = XML(xml_id, valor, data, cnpj, nome_fantasia)
                XmlRepositorio.inserir(xml)


