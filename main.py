from robo.nota_fiscal_paulista import NotaFiscalPaulista
from read_xml import ReadXmls

id   = ReadXmls('teste.xml')
robo = NotaFiscalPaulista('21242425802','050579')
robo.login()
robo.salvarCupom('35190224684575000309590004165900147942795151')
# robo.close()
