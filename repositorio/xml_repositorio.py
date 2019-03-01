from conexao.factory import Factory

class XmlRepositorio():

    @staticmethod
    def inserir(xml):
      db     = Factory.Conectar()
      cursor = db.cursor()
      try:
        db.begin()
        query  = "INSERT INTO xmls (" \
                 " cod_xml, " \
                 " cnpj, " \
                 " data, " \
                 " valor, " \
                 " nome_fantasia" \
                 " ) " \
                 "VALUES (" \
                 " %(cod_xml)s," \
                 " %(cnpj)s," \
                 " %(data)s," \
                 " %(valor)s," \
                 " %(nome_fantasia)s" \
                 ")"
        cursor.execute(
            query,
            (
              {
               'cod_xml'      : xml.cod_xml,
               'cnpj'         : xml.cnpj,
               'data'         : xml.data,
               'valor'        : xml.valor,
               'nome_fantasia': xml.nome_fantasia
              }
            )
        )
        db.commit()
      except:
        db.close()

    @staticmethod
    def select():
        db = Factory.Conectar()
        cursor = db.cursor()
        try:
            db.begin()
            query = "SELECT * FROM xmls"
            cursor.execute(query)
            return cursor.fetchall()
        except:
            db.close()

    @staticmethod
    def select_xml_by_cod(cod):
        db = Factory.Conectar()
        cursor = db.cursor()
        try:
            db.begin()
            query = "SELECT * FROM xmls WHERE cod_xml = %(cod)s"
            cursor.execute(query,({'cod': cod}))
            if cursor.fetchone():
                return False
            else:
                return True
        except:
            db.close()

    @staticmethod
    def select_xml_by_month():
        db = Factory.Conectar()
        cursor = db.cursor()
        try:
            db.begin()
            query = "SELECT * FROM xmls WHERE status = 'AP' and extract(month FROM data) = month(now()) and extract(year FROM data) = year(now())";
            cursor.execute(query)
            return cursor.fetchall()
        except:
            db.close()
