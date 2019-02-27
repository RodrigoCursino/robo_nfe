import MySQLdb, configparser

class Factory():

    @staticmethod
    def Conectar(self):

        config = configparser.ConfigParser()
        config.read('./conexao.ini')

        db = MySQLdb.connect(
            user=config['DATABASE']['user'],
            passwd=config['DATABASE']['passwd'],
            db=config['DATABASE']['db'],
            host=config['DATABASE']['host'],
            port=config['DATABASE']['port'],
            autocommit=config['DATABASE']['autocommit'],
        )

        return db
