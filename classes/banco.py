class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []
        
    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)
        
    def inserir_contas(self, conta):
        self.contas.append(conta)
        
    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False
        
        if cliente.conta.agencia not in self.agencias:
            return False
        
        return True