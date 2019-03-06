from entidades import pessoa

class PessoaRepositorio():

    @staticmethod
    def retunPessoa(nome):
        if nome == 'tony':
            return pessoa.Pessoa('21242425802','050579')