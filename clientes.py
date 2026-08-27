import persistencia


def cadastrar_cliente(clientes):

    print("\n--- CADASTRAR CLIENTE ---")

    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone: ")

    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    clientes.append(cliente)

    persistencia.salvar("clientes.json", clientes)

    print("Cliente cadastrado!")


def listar_clientes(clientes):

    print("\n--- CLIENTES CADASTRADOS ---")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")

    else:

        for cliente in clientes:
            print("-------------------------")
            print("Nome:", cliente["nome"])
            print("Telefone:", cliente["telefone"])
