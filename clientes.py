import persistencia


def cadastrar_jogo(jogos):

    print("\n--- CADASTRAR JOGO ---")

    titulo = input("Digite o título do jogo: ")
    plataforma = input("Digite a plataforma: ")
    genero = input("Digite o gênero: ")
    valor = float(input("Digite o valor da diária: R$ "))
    copias = int(input("Digite a quantidade de cópias: "))

    jogo = {
        "titulo": titulo,
        "plataforma": plataforma,
        "genero": genero,
        "valor": valor,
        "copias": copias
    }

    jogos.append(jogo)

    persistencia.salvar("jogos.json", jogos)

    print("Jogo cadastrado!")


def listar_jogos(jogos):

    print("\n--- JOGOS CADASTRADOS ---")

    if len(jogos) == 0:
        print("Nenhum jogo cadastrado.")
    else:

        for jogo in jogos:
            print("-------------------------")
            print("Título:", jogo["titulo"])
            print("Plataforma:", jogo["plataforma"])
            print("Gênero:", jogo["genero"])
            print("Valor por dia: R$", jogo["valor"])
            print("Cópias disponíveis:", jogo["copias"])
