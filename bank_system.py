import textwrap

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Conta:
    def __init__(self, numero, agencia, usuario):
        self.numero = numero
        self.agencia = agencia
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.limite_saques = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:	R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Saldo insuficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Valor excede o limite por saque. @@@")
        elif self.numero_saques >= self.limite_saques:
            print("\n@@@ Limite de saques diários atingido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:		R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Valor inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print(self.extrato if self.extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo:		R$ {self.saldo:.2f}")
        print("==========================================")


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.AGENCIA = "0001"

    def menu(self):
        while True:
            opcao = input(textwrap.dedent("""
            ================ MENU ================
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [nu] Novo usuário
            [nc] Nova conta
            [lc] Listar contas
            [q] Sair
            => """))

            if opcao == "d":
                self.operacao_deposito()
            elif opcao == "s":
                self.operacao_saque()
            elif opcao == "e":
                self.operacao_extrato()
            elif opcao == "nu":
                self.criar_usuario()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "q":
                break
            else:
                print("@@@ Operação inválida. Tente novamente. @@@")

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if self.buscar_usuario_por_cpf(cpf):
            print("@@@ Usuário já existente. @@@")
            return

        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

        self.usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do titular: ")
        usuario = self.buscar_usuario_por_cpf(cpf)

        if not usuario:
            print("@@@ Usuário não encontrado. @@@")
            return

        numero = len(self.contas) + 1
        conta = Conta(numero, self.AGENCIA, usuario)
        self.contas.append(conta)
        print("=== Conta criada com sucesso! ===")

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 50)
            print(f"Agência:	{conta.agencia}")
            print(f"C/C:		{conta.numero}")
            print(f"Titular:	{conta.usuario.nome}")

    def buscar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def selecionar_conta(self):
        cpf = input("Informe o CPF do titular da conta: ")
        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                return conta
        print("@@@ Conta não encontrada. @@@")
        return None

    def operacao_deposito(self):
        conta = self.selecionar_conta()
        if conta:
            valor = float(input("Valor do depósito: "))
            conta.depositar(valor)

    def operacao_saque(self):
        conta = self.selecionar_conta()
        if conta:
            valor = float(input("Valor do saque: "))
            conta.sacar(valor)

    def operacao_extrato(self):
        conta = self.selecionar_conta()
        if conta:
            conta.exibir_extrato()


if __name__ == "__main__":
    banco = Banco()
    banco.menu()
