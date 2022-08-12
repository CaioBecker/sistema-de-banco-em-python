from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

cp = ContaPoupanca(111, 10, 0)

cp.depositar(100)

cp.sacar(5)

print('##########################')


cp = ContaCorrente(111, 10, 0)

cp.depositar(100)

cp.sacar(200)