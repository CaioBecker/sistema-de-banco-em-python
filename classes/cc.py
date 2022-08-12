from tkinter import E
from tkinter.tix import ExFileSelectBox
from classes.conta  import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo) 
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite
    
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo Insuficiente')
            return
        if not isinstance(valor, (int,float)):
            raise ValueError("Saldo precisa ser numerico")
        
        self.saldo -= valor
        self.detalhes()
    
        
    