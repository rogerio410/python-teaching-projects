class ContaBancaria():

    def __init__(self, titular, senha, numero):
        self.numero = numero
        self.saldo = 0.0
        self.titular = titular
        self.senha = senha
        self.agencia = '001'

    def depositar(self, valor):
        if valor >= 0 and valor <= 3000:
            self.saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        self.saldo -= valor

    def transferir(self, outra_conta, valor):
        pass


class Titular():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class ContaCorrente(ContaBancaria):

    def __init__(self, titular, senha, numero, limite=300):
        super().__init__(titular, senha, numero)
        self.limite = limite

    def depositar(self, valor):
        valor *= 0.99
        return super().depositar(valor)


class ContaPoupanca(ContaBancaria):

    def render(self, tx=0.0056):
        super().depositar(self.saldo * tx)


class ContaDigital():

    def __init__(self, titular, senha, numero):
        self.conta_corrente = ContaCorrente(titular, senha, numero, 250)

    def depositar(self, valor):
        self.conta_corrente.depositar(valor)

    def transferir(self, conta_destino, valor):
        self.transferir(conta_destino, valor)
