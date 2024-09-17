from abc import ABC, abstractmethod
import random

class Conta(ABC):
    @abstractmethod
    def consultar_saldo(self):
        ... # as reticencias servem como o comando pass
        
    @abstractmethod
    def fazer_deposito(self, valor):
        pass
    
    @abstractmethod
    def fazer_saque(self, valor):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
        
    @property
    def conta(self):
        return self.__conta
    
    @conta.setter
    def conta(self, conta):
        self.__conta = conta
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        
    def consultar_saldo(self):
        return self.__saldo
   
    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def fazer_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo
class GeradorDeContas:
    def __init__(self):
        self.contas = set()  # Armazena números de conta gerados

    def gerar_numero_conta(self):
        numero_conta = random.randint(1000, 9999)  # Gera um número de conta de 4 dígitos
        while numero_conta in self.contas:
            numero_conta = random.randint(1000, 9999)  # Garante que seja único
        self.contas.add(numero_conta)  # Adiciona o número ao conjunto
        return numero_conta


