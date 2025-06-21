def mostrar_menu():
    menu = """
    ==========================
        MENU - BANCO DIGITAL
    ==========================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================

    => """
    return input(menu)

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Saldo insuficiente.")

    elif excedeu_limite:
        print(f"O valor máximo por saque é R$ {limite:.2f}.")

    elif excedeu_saques:
        print(f"Limite diário de {LIMITE_SAQUES} saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor inválido para saque.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("============================\n")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo... Obrigado por usar nosso banco!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()