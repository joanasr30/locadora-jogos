import persistencia
import jogos
import clientes
import locacoes


jogos_cadastrados = persistencia.carregar("jogos.json")
clientes_cadastrados = persistencia.carregar("clientes.json")
locacoes_realizadas = persistencia.carregar("locacoes.json")


while True:

    print("--- LOCADORA DE JOGOS ---")
 
    print("[1] - Cadastrar jogo")
    print("[2] - Listar jogos")
    print("[3] - Cadastrar cliente")
    print("[4] - Listar clientes")
    print("[5] - Fazer locação")
    print("[6] - Listar locações")
    print("[0] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        jogos.cadastrar_jogo(jogos_cadastrados)

    elif opcao == "2":

        jogos.listar_jogos(jogos_cadastrados)

    elif opcao == "3":

        clientes.cadastrar_cliente(clientes_cadastrados)

    elif opcao == "4":

        clientes.listar_clientes(clientes_cadastrados)

    elif opcao == "5":

        locacoes.fazer_locacao(
            jogos_cadastrados,
            clientes_cadastrados,
            locacoes_realizadas
        )

    elif opcao == "6":

        locacoes.listar_locacoes(locacoes_realizadas)

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")
