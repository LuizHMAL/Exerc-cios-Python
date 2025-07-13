class Conta():
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self._extrato = []
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self._extrato.append(f"Depositado: R$ {valor}")
            self._extrato.append(f"Saldo Atual: R$ {self.__saldo}")
        else:
            print("Valor inválido")
        
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            self._extrato.append(f"Saque: R$ {valor}")
            self._extrato.append(f"Saldo Atual: R$ {self.__saldo}")
        else:
            print("Saldo insuficiente")
    
    def transferir(self, valor: float, destino):
        if self.__saldo >= valor:
            self.__saldo -= valor
            destino.depositar(valor)
            self._extrato.append(f"Transferido: R$ {valor} para {destino.titular}")
            self._extrato.append(f"Saldo Atual: R$ {self.__saldo}")
        else:
            print("Saldo insuficiente")

conta1 = Conta(1, "Marcos", 4000)
conta2 = Conta(2, "João", 2000)

conta1.transferir(2000, conta2)

print(conta1._extrato)
print(conta2._extrato)