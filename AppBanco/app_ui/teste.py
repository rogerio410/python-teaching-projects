from modelo.model import *

def main():

    titular = Titular('Rogerio', 123)

    conta = ContaBancaria(titular, 123, 12)
    conta_corrente = ContaCorrente(titular, 123, 4, 1000)
    conta_corrente2 = ContaCorrente(titular, 123, 4)
    conta_poupanca = ContaPoupanca(titular, 1234, 1234)
    conta_digital = ContaDigital(titular, 12, 12)

    conta.depositar(1000)
    conta_corrente.depositar(1000)
    conta_corrente2.depositar(1000)
    conta_poupanca.depositar(1000)
    conta_digital.depositar(300)

    conta_poupanca.render()

    conta_digital.sacar(295)

    print('CP: %.4f' % conta_poupanca.saldo)
    print('CB:', conta.saldo)
    print('CC', conta_corrente.saldo+conta_corrente.limite)
    print('CC', conta_corrente2.saldo+conta_corrente2.limite)
    print('CD', conta_digital.saldo+conta_digital.limite)


if __name__ == '__main__':
    main()