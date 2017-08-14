#1) Uma tarefa pertence a um projeto
#
#2) Tarefa possui os atributos:
#   -descrição;
#   -data Inicio;
#   -data Fim;
#   -prioridade;
#
#3) Uma tarefa é solicitada por uma Pessoa Juridica
#   e atendida por uma pessoa Física;

class Projeto():

    def __init__(self, nome = None, data_criacao = None):
        self.nome = nome
        self.data_criacao = data_criacao
        self.tarefa = Tarefa('')

class Tarefa():
    def __init__(self, nome, descricao, data_inicio, data_fim, prioridade):
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.prioridade = prioridade
    
class Endereco():

    def __init__(self, log = None, estado = None):
        self.log = log
        self.estado = estado

class Pessoa():

    def __init__(self, nome = None, data_nascimento = None, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.end = endereco

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):

    def __init__(self, cpf, nome, data_nascimento, endereco):
        Pessoa.__init__(self, nome, data_nascimento, endereco)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome, data_nascimento, endereco):
        Pessoa.__init__(self, nome, data_nascimento, endereco)
        self.cnpj = cnpj

class Solicitar():
    def __init__(self):
        self.p_juridica = PessoaJuridica()
        self.projeto = Projeto()

class Executar():
    def __init_(self):
        self.solicitacao = Solicitar()
        self.p_fisica = PessoaFisica()
