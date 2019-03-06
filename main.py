from robo.nota_fiscal_paulista import NotaFiscalPaulista
from repositorio import pessoa_repositorio
from servicos import read_dir
import sys

#nome = sys.argv[1]
nome = 'tony'
user = pessoa_repositorio.PessoaRepositorio.retunPessoa(nome)
read = read_dir.ReadDirectory('data')

listagem_xml = read.read()

robo = NotaFiscalPaulista(user.cpf,user.senha)
robo.login()
for lista in listagem_xml:
    robo.salvarCupom(lista.cod_xml)
robo.close()
