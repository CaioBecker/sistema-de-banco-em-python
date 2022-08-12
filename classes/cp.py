from tkinter import E
from tkinter.tix import ExFileSelectBox
from classes.conta  import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return
        if not isinstance(valor, (int,float)):
            raise ValueError("Saldo precisa ser numerico")
        
        self.saldo -= valor
        self.detalhes()
    
        
    