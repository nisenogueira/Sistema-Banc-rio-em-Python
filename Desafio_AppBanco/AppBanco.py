menu =  """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """ 
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor invalido, digite novamente")

    elif opcao == "2":
        valor = float(input("Saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente") 
        elif excedeu_limite:
            print("Limite de saque excedido")
        elif excedeu_saques:
            print("Limite de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor invalido, digite novamente")

    elif opcao == "3":
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=======================================")
    elif opcao == "0":
        break
    else:
        print("Opcao invalida, digite novamente")