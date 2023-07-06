menu = """
Informe a operação que deseja realizar:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

: """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUE  = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é invalido.')
    
    elif opcao == "s":
        valor = float(input('Digite o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques > LIMITE_SAQUE

        if excedeu_saldo:
            print('\nDesculpe! Você não tem saldo em conta suficiente.')
        elif excedeu_limite:
            print('\nDesculpe! Você ultrapassou o valor limite por saque.')
        elif excedeu_saques:
            print('\nDesculpe! Você ultrapassou o numéro de saques diários.')
        elif valor > 0:
           saldo -= valor
           extrato += f'Saque: R$ {valor:.2f}\n' 
           num_saques += 1
        else:
            print('Desculpe! Valor inválido.')
    
    elif opcao == "e":
        print(f"\n{15*'='}EXTRATO{15*'='}")
        print('Não há movimentações em sua conta.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print(f"\n{(30 + len('extrato')) *'='}")
    
    elif opcao == "q":
        break

    else:
       print('Operação inválida!')