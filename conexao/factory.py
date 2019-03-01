import MySQLdb, configparser

class Factory():


    # @staticmethod
    # def Conectar():
    #     config = configparser.ConfigParser()
    #     config.read('../conexao.ini')
    #
    #     db = MySQLdb.connect(user=config['DATABASE']['user'],
    #                          passwd=config['DATABASE']['passwd'],
    #                          db=config['DATABASE']['db'],
    #                          host=config['DATABASE']['host'],
    #                          port=int(config['DATABASE']['port']),
    #                          autocommit=config['DATABASE']['autocommit'])
    #
    #     return db

    @staticmethod
    def Conectar():
        config = configparser.ConfigParser()
        config.read('conexao.ini')

        db = MySQLdb.connect(user='root',
                             passwd='tmontec',
                             db='robo',
                             host='localhost',
                             port=3306,
                             autocommit=True)

        return db
