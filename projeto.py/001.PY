# Criando Sistema Bancário

def menu():
    print('=' * 25)
    print('{:^25}' .format('Banco EL'))
    return """
    ====== MENU =====
    [d]\tDepositar
    [s]\tSaque
    [e]\tExtrato
    [nc] Nova Conta
    [nu] Novo Usuario
    [lc] Listar Contas
    [x]\tSair
    ==>> """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito: R${valor:.2f}\n')
        print(f"\n=== Depósito de R$ {valor:.2f} realizado! ===")
    else:
        print("\n@@@ Erro: Valor inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saque >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Erro: Saldo insuficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Erro: Valor excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Erro: Número máximo de saques atingido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:\tR$ {valor:.2f}\n")
        num_saque += 1
        print(f"\n=== Saque de R$ {valor:.2f} realizado! ===")
    else:
        print("\n@@@ Erro: Valor inválido. @@@")
    
    return saldo, extrato, num_saque

def exibir_extrato(saldo, /, *, extrato):
    print("\n=== EXTRATO ===")
    print("\n".join(extrato) if extrato else "Sem movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=" * 20)

def criar_usuario(usuarios):
    cpf = input('Informe o seu CPF (APENAS NÚMEROS): ')
    if filtrar_usuarios(cpf, usuarios) is not None:
        print('\n@@@ Já existe um usuário com esse CPF! @@@')
        return
    
    nome = input('Digite seu Nome: ')
    data_nasc = input ('Digite sua Data de Nascimento (dd-mm-aaaa): ')
    endereco = input("Informe o seu Endereço (logradouro, num - bairro - cidade/estado): ")

    usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})
    print('=== Usuário criado com sucesso! ===')

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input('Informe o seu CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n=== Conta Criada com SUCESSO! ===')
        return {'agencia': agencia, 'num_conta': num_conta, 'usuario': usuario}
    
    print('\n@@@ Usuário inexistente, fluxo de criação de conta ENCERRADO. @@@')
    return None

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    
    for conta in contas:
        print("=" * 50)
        print(f"Agência:	{conta['agencia']}")
        print(f"C/C:		{conta['num_conta']}")
        print(f"Titular:	{conta['usuario']['nome']}")
    print("=" * 50)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = []
    num_saque = 0
    usuarios = []
    contas = []

    while True:
        op = input(menu()).strip().lower()

        if op == 'd':
            valor = float(input('Informe o valor do Depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif op == 's':
            valor = float(input('Informe o valor do Saque: '))
            saldo, extrato, num_saque = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saque=num_saque,
                limite_saques=LIMITE_SAQUE
            )

        elif op == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif op == 'nu':
            criar_usuario(usuarios)

        elif op == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif op == 'lc':
            listar_contas(contas)
        
        elif op == 'x':
            print("\nSaindo do sistema bancário. Obrigado por utilizar o Banco EL!")
            break

main()
