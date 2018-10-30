from servico.banco_service import Banco


def main():

    banco = Banco('NuBranco')
    conta_logada = None


    menu = '*** BANCO ***' \
           '\n1 - Abrir Conta' \
           '\n2 - Depositar via Envelope' \
           '\n0 - Fechar'

    while True:
        opcao = int(input(menu))

        if opcao == 1: # abrir conta
            cpf = input('CPF: ')
            nome = input('NOME: ')
            senha, e_confirmacao = map(str, input('Senha e Confirm.: ').split())

            if senha == e_confirmacao:
                banco.nova_conta(nome, cpf, senha)
                print('Conta aberta com sucesso')
            else:
                print('Dados Inválidos!!!')
        if opcao == 2:
            numero_conta = int(input('N. Conta: '))
            valor = float(input('Valor R$: '))
            if banco.depositar(numero_conta, valor):
                print('Ok')
            else:
                print('Not OK')

            for conta in banco.contas:
                if conta.numero == numero_conta:
                    conta.depositar(valor)
        if opcao == 0:
            break

if __name__ == '__main__':
    main()