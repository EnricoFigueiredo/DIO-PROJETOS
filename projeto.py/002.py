from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
 
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
    @property
    def saldo(self):
        return self._saldo   
    
    @property
    def numero(self):
        return self._numero   
    
    @property
    def agencia(self):
        return self._agencia   
    
    @property
    def cliente(self):
        return self._cliente   
    
    @property
    def historico(self):
        return self._historico   
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operaçao falhou! Voce nao tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso!")
            return True
        
        else:
            print("\n@@@ Operaçao falhou! O valor informado e invalido")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n@@@ Deposito realizado com sucesso! @@@")
        else:
            print("\n@@@ Operaçao falhou! valor informado invalido @@@")
            return False
        
        return True

class ContaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saque = len(
            [transacao for transacao in self.historico.
             transacao if transacao["tipo"] == Saque.
             __name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saque > self.limite_saque

        if excedeu_limite:
            print("\n@@@ Operaçao falhou! @@@")

        elif excedeu_saque:
            print("\n Operaçao falhou! numero de saque excedio")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
    """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoe.append(
        {"tipo": transacao.__class__.__name__,
         "valor": transacao.valor,
         "data": datetime.now().strftime
         ("%d-%n-%Y %H:%M:%s"),
         })
        
class transacao():
    @property
    def valor(self):
        pass
    def registrar(self,conta):
        pass

class Saque(transacao):
    def __init__(self,valor):
        return self.valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class deposito(transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)