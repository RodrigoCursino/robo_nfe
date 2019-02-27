from conexao.factory import Factory

class XmlRepositorio():

    def inserir(self, xml):
      db     = Factory.Conectar()
      cursor = db.cursor()
      try:
        db.begin()
        query  = "INSERT INTO xmls (cod_xml, cnpj, data, valor) VALUES (%(cod_xml)s,%(cnpj)s,%(data)s,%(valor)s)"
        cursor.execute(
            query,
            ({'cod_xml': xml.cod_xml,'cnpj': xml.cnpj, 'data': xml.data, 'valor': xml.valor})
        )
        db.close()
      except:
          print("Sql Error")


