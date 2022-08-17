from classes.banco import Banco
from classes.cc import ContaCorrente
from classes.cliente import Cliente
from classes.conta import Conta
from classes.cp import ContaPoupanca
from classes.pessoa import Pessoa

banco = Banco()

cliente1 = Cliente('luiz', 30)

cliente2 = Cliente('Maria', 18)

cliente3 = Cliente('João', 50)        

conta1 = ContaPoupanca(1111, 254136, 0)

conta2 = ContaCorrente(2222, 254137, 0)

conta3 = ContaPoupanca(1313, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print("Cliente invalido")

