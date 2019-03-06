import os
from servicos import read_xml


class ReadDirectory():

    def __init__(self, directory):
        self.__directory = directory


    def read(self):

        list_xml = []
        files = os.listdir('./'+self.__directory)

        for file in files:
            read  = read_xml.ReadXmls(file)
            if read.loadFiles() != None:
                list_xml.append(read.loadFiles())

        return list_xml