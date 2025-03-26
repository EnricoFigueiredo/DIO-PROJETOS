# Criando Sistema Bancário
print('=' * 25)
print('{:^25}' .format('Banco EL'))
print('=' * 25)

nome = input(('Digite seu nome: '))
extrato, saldo, num_saque = [], 0, 0
limite, LIMITE_SAQUE = 500, 3


menu = "\n[d] Depositar  [s] Sacar  [e] Extrato  [q] Sair\n=> "

def depositar(valor):
     global saldo
     if valor > 0:
          saldo += valor
          extrato.append(f'Deposito: R${valor:.2f}\n')
          print(f"Depósito de R$ {valor:.2f} realizado!")
     else: 
        print("Erro: Valor inválido.")

def sacar(valor):
    global saldo, num_saque
    if valor > saldo:
        print("Erro: Saldo insuficiente.")
    elif num_saque >= LIMITE_SAQUE:
        print("Erro: Limite de saques excedido.")
    elif valor > limite:
        print("Erro: Valor excede o limite.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        num_saque += 1
        print(f"Saque de R$ {valor:.2f} realizado!")
    else:
        print("Erro: Valor inválido.")


def exibir_extrato():
    print("\n=== EXTRATO ===")
    print("\n".join(extrato) if extrato else "Sem movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=" * 20)

while True:
    op = input(menu).lower()
    if op == "d":
        depositar(float(input("Valor do depósito: ")))
    elif op == "s":
        sacar(float(input("Valor do saque: ")))
    elif op == "e":
        exibir_extrato()
    elif op == "q":
        print("Obrigado por usar o Banco EL!")
        break
    else:
        print("Opção inválida. Escolha novamente.")

