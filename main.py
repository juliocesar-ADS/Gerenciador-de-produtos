import time


# lista dos valores

estoque = []

#adicionar produtos
def adicionar():
    print(" ________________________\n"
          "|  CADASTRO DE PRODUTOS  |\n"
          "|________________________|\n")

    itens = int(input("Quantos itens você deseja cadastrar? "))

    for i in range(itens):
        estoque.append(input("\nColoque o produto que deseja:\n"))
    print("\n\033[32mCADASTRO CONCLUIDO...\033[0m")
    time.sleep(1)

#remover itens da lista
def delete():
    while True:
        print("| REMOVER ITEM |")
        remover = input("Digite o nome do produto: ")
        if remover in estoque:
            estoque.remove(remover)
            time.sleep(1)
            print("PRODUTOS ATUALIZADOS...")
        else:
            print("PRODUTO INVALIDO\n")
        sair_remover = int(input("| Deseja remover mais produtos? |\n"
                                    "|          [1] SIM              |\n"
                                    "|          [2] NÃO              |\n"))
        if sair_remover == 2:
            print("VOLTANDO...")
            time.sleep(1)
            break
        else:
            print("Numero invalido")

#visualizar lista de produtos
def visualizar():
    print("| VISUALIZAR ITEM |")
    endereco = 1
    for itens in estoque:
        print(endereco, "-", itens, end="\n")
        endereco += 1
    time.sleep(3)

#sair do programa
def sair():
    time.sleep(1)
    print("|  ESPERO QUE TENHA GOSTADO DO PROTÓTIPO,  | \n"
            "|  SEMPRE ABERTO A FEEDBACKS               | \n"
            "|  ATÉ A PROXIMA                           |")
    time.sleep(1)



while True:

    time.sleep(1)

    print(""
          "    _____________________________\n"
          "   |   GERENCIADOR DE PRODUTOS   |\n"
          "   |_____________________________|\n"
          "   |                             |\n"
          "   |   [1] ADICIONAR PRODUTO     | \n"
          "   |   [2] DELETAR PRODUTO       | \n"
          "   |   [3] VISUALIZAR PRODUTO    |\n"
          "   |   [4] SAIR                  |\n"
          "   |_____________________________|\n")

    time.sleep(1)
    try:
        inicio = input("Digite o numero da opção que você quer selecionar: ")

        if inicio != "1" and inicio != "2" and inicio != "3" and inicio != "4":
            print("OPÇÃO INVALIDA...")
            continue

        # adicionar produtos

        else:
            if inicio == "1":
                adicionar()

    # remover os produtos

            if inicio == "2":
                delete()

    # visualizar produtos

            if inicio == "3":
                visualizar()

    # sair do programa

            if inicio == "4":
                sair()
                break

    except ValueError:
        print("\n\033[31mAlgum valor errado, tente novamente...\033[0m")
        time.sleep(1)
