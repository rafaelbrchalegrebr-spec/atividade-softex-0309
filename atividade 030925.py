print("Bem-vindos ao Cinema UTEC!")

total_ingressos_vendidos = 0
valor_total_vendas = 0.0

while True:
    # Pergunta a quantidade de ingressos
    qtd = int(input("\nQuantos ingressos deseja comprar? "))

    total = 0.0  # total apenas dessa venda

    if qtd > 1:
        # Para mais de um ingresso, pergunta quantos são crianças e estudantes
        qtd_criancas = int(input("Quantos desses ingressos são para crianças (até 12 anos)? "))
        while qtd_criancas > qtd or qtd_criancas < 0:
            print("Quantidade inválida. Tente novamente.")
            qtd_criancas = int(input("Quantos desses ingressos são para crianças (até 12 anos)? "))

        qtd_restante = qtd - qtd_criancas

        qtd_estudantes = int(input("Quantos dos restantes são para estudantes com carteira válida? "))
        while qtd_estudantes > qtd_restante or qtd_estudantes < 0:
            print("Quantidade inválida. Tente novamente.")
            qtd_estudantes = int(input("Quantos dos restantes são para estudantes com carteira válida? "))

        qtd_adultos = qtd - qtd_criancas - qtd_estudantes

        # Calcula os valores
        total += qtd_criancas * 15.00
        total += qtd_estudantes * 15.00
        total += qtd_adultos * 30.00

        # Mostra o resumo parcial
        print(f"\nIngressos infantis (R$15,00): {qtd_criancas}")
        print(f"Ingressos de estudantes (R$15,00): {qtd_estudantes}")
        print(f"Ingressos normais (R$30,00): {qtd_adultos}")

    else:
        # Venda unitária: faz as perguntas individualmente
        idade = int(input("Por favor, digite a idade do cliente: "))

        if idade <= 12:
            preco = 15.00
            print(f"Preço infantil, valor: R$ {preco:.2f}")
        else:
            estudante = input("Você é estudante com carteira válida? (S/N): ").strip().lower()
            if estudante == "s":
                preco = 15.00
                print(f"Preço estudante, valor: R$ {preco:.2f}")
            else:
                preco = 30.00
                print(f"Preço normal / Adulto, valor: R$ {preco:.2f}")

        total += preco

    # Atualiza os totais gerais
    total_ingressos_vendidos += qtd
    valor_total_vendas += total

    # Resumo da compra
    print("\n=== Resumo da Compra ===")
    print(f"Quantidade de ingressos: {qtd}")
    print(f"Total a pagar: R$ {total:.2f}")

    # Pergunta se deseja nova venda
    nova_venda = input("\nDeseja registrar uma nova venda? (S/N): ").strip().lower()
    if nova_venda != "s":
        break

# Encerramento
print("\n=== Fim de expediente ===")
print(f"Total de ingressos vendidos: {total_ingressos_vendidos}")
print(f"Valor total das vendas: R$ {valor_total_vendas:.2f}")