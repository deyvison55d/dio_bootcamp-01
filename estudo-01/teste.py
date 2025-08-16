"""
Criar um sistema bancario simples que permita:
1. Saque
2. Deposito
3. Extrato

O sistema deve permitir no máximo 3 saques diários, com limite de R$500,00 por saque.
Caso não tenha saldo suficiente, o sistema deve informar o usuário.
Todos os saques devem ser armazenados numa váriavel e exibidos no extrato.
Extrato deve conter todos os saques e depósitos realizados no formato R$0.00"""

from menu import *
from funções import *

saques_diarios = 3
saldo = 0
while True:
    menu(saldo)
    try:
        opção = int(input('Escolha uma opção: '))

        if opção < 1 or opção > 4:
            print('Opção inválida. Tente novamente.')
            continue # Loop para garantir que a opção esteja entre 1 e 3


        if opção == 1: # Depósito
            valor = input('Digite o valor do depósito: '.strip())
            saldo = deposito(valor,saldo)
            

        elif opção == 2: # Saque
            if saques_diarios <= 0:
                print('Limite de saques diários atingido. Tente novamente amanhã.')
                continue
            valor = input('Digite o valor do saque: '.strip())
            saldo, saque = saque(valor, saldo, saques_diarios)
        

        elif opção == 3: # Extrato
            print('Extrato Bancário:')
            extratos = extrato()
            for item in extratos:
                print(item)


        elif opção == 4: # Sair
            print('Saindo do sistema. Até logo!')
            break

    except ValueError:
        print('Valor inválido. Por favor, insira um número inteiro.')
    