import persistencia


def fazer_locacao(jogos, clientes, locacoes):

    print("\n--- FAZER LOCAÇÃO ---")

    if len(clientes) == 0:
        print("Não existem clientes cadastrados.")
        return

    if len(jogos) == 0:
        print("Não existem jogos cadastrados.")
        return

    print("\nClientes:")

    for i in range(len(clientes)):
        print(i + 1, "-", clientes[i]["nome"])

    cliente = int(input("Escolha o cliente: "))

    if cliente < 1 or cliente > len(clientes):
        print("Cliente inválido.")
        return

    print("\nJogos:")

    for i in range(len(jogos)):
        print(
            i + 1,
            "-",
            jogos[i]["titulo"],
            "- Cópias:",
            jogos[i]["copias"]
        )

    jogo = int(input("Escolha o jogo: "))

    if jogo < 1 or jogo > len(jogos):
        print("Jogo inválido.")
        return

    jogo = jogo - 1
    cliente = cliente - 1

    if jogos[jogo]["copias"] <= 0:
        print("Não existem cópias disponíveis.")
        return

    dias = int(input("Digite a quantidade de dias: "))

    if dias <= 0:
        print("Quantidade de dias inválida.")
        return

    valor = dias * jogos[jogo]["valor"]

    if dias > 7:
        desconto = valor * 0.10

    elif dias > 3:
        desconto = valor * 0.05

    else:
        desconto = 0

    valor_final = valor - desconto

    locacao = {
        "cliente": clientes[cliente]["nome"],
        "jogo": jogos[jogo]["titulo"],
        "dias": dias,
        "valor_final": valor_final
    }

    locacoes.append(locacao)

    jogos[jogo]["copias"] = jogos[jogo]["copias"] - 1

    persistencia.salvar("locacoes.json", locacoes)
    persistencia.salvar("jogos.json", jogos)

    print("\n--- LOCAÇÃO REALIZADA ---")
    print("Cliente:", clientes[cliente]["nome"])
    print("Jogo:", jogos[jogo]["titulo"])
    print("Dias:", dias)
    print("Valor sem desconto: R$", valor)
    print("Desconto: R$", desconto)
    print("Valor final: R$", valor_final)
    print("Cópias restantes:", jogos[jogo]["copias"])


def listar_locacoes(locacoes):

    print("\n--- LOCAÇÕES REALIZADAS ---")

    if len(locacoes) == 0:
        print("Nenhuma locação realizada.")

    else:

        for locacao in locacoes:
            print("Cliente:", locacao["cliente"])
            print("Jogo:", locacao["jogo"])
            print("Dias:", locacao["dias"])
            print("Valor final: R$", locacao["valor_final"])
