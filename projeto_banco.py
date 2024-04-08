historico_deposito = []
historico_saque = []
saldo_da_conta = 0
soma_saque = 0

while True:
    operacao_desejada = int(input("Operação desejada\n[1] Depósito\n[2] Saque\n[3] Extrato\n"))

    if operacao_desejada == 1:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        historico_deposito.append(valor_deposito)  # Adiciona o valor ao histórico de depósitos
        saldo_da_conta += valor_deposito  # Atualiza o saldo da conta com o valor depositado
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")

    elif operacao_desejada == 2:
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= 500:
            if saldo_da_conta >= valor_saque:
                historico_saque.append(valor_saque)  # Adiciona o valor ao histórico de saques
                saldo_da_conta -= valor_saque  # Atualiza o saldo da conta após o saque
                soma_saque += valor_saque  # Atualiza a soma total dos saques realizados
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor superior a R$500. Digite um valor até R$500.")

    elif operacao_desejada == 3:
        print(f"Extrato:")
        print(f"- VALORES DEPOSITADOS: {historico_deposito}")
        print(f"- VALORES SACADOS: {historico_saque}")
        print(f"Saldo atual da conta: R${saldo_da_conta:.2f}")

    else:
        print("Operação inválida. Por favor, escolha uma opção válida.")

    continuar = input('Deseja continuar? (S/N): ').lower()
    if continuar == 'n':
        break

print("Encerrando o programa. Obrigado!")
