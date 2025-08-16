def deposito(valor,saldo):
    """
    Função para realizar depósito em uma conta bancária.

    Parameters:
        valor (float): Valor a ser depositado.
        saldo (float): Saldo atual da conta.

    Returns:
        saldo (float): Novo saldo após o depósito.
    """
    while True:
        try:
            valor = int(valor)
            if valor <= 0:
                print('\033[31mValor inválido. O depósito deve ser maior que zero.\033[m')
            
            else:
                saldo += valor
                print(f'\033[33mDepósito\033[m de \033[32mR${valor:.2f}\033[m realizado com sucesso.')
                extrato(f'Depósito: R${valor:.2f}')
                return saldo # Retorna o novo saldo
        
        except ValueError:
            print('\033[31mValor inválido. Por favor, insira um número inteiro.\033[m')
            valor = input('Digite o valor do depósito: ')


def saque(valor, saldo, saques_diarios):
    """
    Função para realizar saque em uma conta bancária.
    
    Parameters:
        valor (int): Valor a ser sacado.
        saldo (int): Saldo atual da conta
        saques_diarios (int): Número de saques diários permitidos.
    
    Returns:
        saldo (int): Novo saldo após o saque.
    """

    if saques_diarios <= 0: # Limite de saques diários atingido
        print('\033[33mLimite de saques diários atingido. Tente novamente amanhã.\033[m')
        return saldo, saques_diarios
    while True:
        try:
            valor = int(valor)
            if valor <= 0:
                print('\033[31mValor inválido. O saque deve ser maior que zero.\033[m')
            
            elif valor > 500: # Limite de saque
                print('\033[31mValor inválido. O saque não pode ser maior que R$500,00.\033[m')
            
            elif valor > saldo: # Verifica se há saldo suficiente
                print('\033[31mSaldo insuficiente para realizar o saque.\033[m')
               
            else:
                saldo -= valor
                print(f'\033[33mSaque\033[m de \033[32mR${valor:.2f}\033[m realizado com sucesso.')
                extrato(f'Saque: R${valor:.2f}')
                saques_diarios -= 1
                return saldo, saques_diarios # Retorna o novo saldo e decrementa saques_diarios
        
        except ValueError:
            print('\033[31mValor inválido. Por favor, insira um número inteiro.\033[m')
            valor = input('Digite o valor do saque: '.strip())

            
def extrato(valor=None):
    """
    Função para exibir o extrato bancário.

    Parameters:
        valor (str, optional): Valor a ser adicionado ao extrato. Se None, apenas retorna o extrato atual.
    
    Returns:
        list: Lista de transações no extrato.
    """

    if not hasattr(extrato, 'lista'):
        extrato.lista = []
    if  valor is not None:
        extrato.lista.append(valor)
    return extrato.lista

    
