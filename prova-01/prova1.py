def anexo():
    def calcular_variacao_percentual(menor, maior):
        if menor > maior:
            menor, maior = maior, menor
        return maior / menor - 1

    def obter_acao_com_maior_variacao_percentual(acao1, acao2):
        simbolo1, _, menor_preco1, maior_preco1 = acao1
        simbolo2, _, menor_preco2, maior_preco2 = acao2

        variacao_percentual1 = calcular_variacao_percentual(menor_preco1, maior_preco1)
        variacao_percentual2 = calcular_variacao_percentual(menor_preco2, maior_preco2)

        if variacao_percentual1 > variacao_percentual2:
            return simbolo1, variacao_percentual1
        else:
            return simbolo2, variacao_percentual2

    def ler_acao():
        simbolo = input("Digite o símbolo da ação: ")
        atual = float(input("Digite o preço atual da ação: "))
        menor = float(input("Digite o menor preço da ação: "))
        maior = float(input("Digite o maior preço da ação: "))
        return simbolo, atual, menor, maior

    print("\n# Ação 1")
    acao1 = ler_acao()

    print("\n# Ação 2")
    acao2 = ler_acao()

    resultado = obter_acao_com_maior_variacao_percentual(acao1, acao2)

    print("Ação com a maior variação percentual:", resultado[0])
    print("Variação percentual da ação:", resultado[1])