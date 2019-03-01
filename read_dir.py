import os
import read_xml
from repositorio.xml_repositorio import XmlRepositorio

files = os.listdir('./data')

for file in files:
    read  = read_xml.ReadXmls(file)
    read.setFile()

