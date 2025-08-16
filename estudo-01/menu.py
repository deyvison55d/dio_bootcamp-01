def linha():
    """
    Função que imprime uma linha de separação.
    """

    print('-' * 40)


def menu(valor):
    """
    Função que exibe o menu do sistema bancário.
    """

    linha()
    banco = f'BANCO PYTHON'.center(40)
    print(f'\033[32m{banco}\033[m')
    linha()
    print(f"""
        Seu Saldo: \033[32mR${valor:.2f}\033[m
        Escolha uma opção:
          \033[33m1 - Depósito
          2 - Saque
          3 - Extrato
          4 - Sair\033[m
          """)
    linha()