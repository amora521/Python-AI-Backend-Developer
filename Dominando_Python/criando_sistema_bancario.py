menu = """

[d] Depositar
[s] Sacar
[p] Pix
[e] Extrato
[q] Sair

=> """

menu_pix = """

[d] Dados bancários
[c] Celular
[e] Email
[a] Chave aleatória
[q] Sair

=> """

saldo = 0
limite = 500
limite_pix = 1000
extrato = ""
numero_saques = 0
numero_pix = 0
LIMITE_SAQUES = 3
LIMITE_PIX = 2

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            print("Operação concluída!")
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque escede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            print("Operação concluída!")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else: 
            print("Operação falhou! O valor informado é invalido.")
    elif opcao == "p":
        
        opcao = input(menu_pix)
        
        valor = float(input("Informe o valor para transferência: "))
        excedeu_saldo = valor > saldo
        excedeu_limite_pix = valor > limite_pix
        excedeu_pix = numero_pix >= LIMITE_PIX
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite_pix:
            print("Operação falhou! O valor de pix escede o limite.")
        elif valor > 0:
            saldo -= valor
            print("Operação concluída!")
            extrato += f"Pix: R$ {valor:.2f}\n"
            numero_pix += 1
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")