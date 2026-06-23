import time
from produtos import *


# lista dos valores

estoque = []

#adicionar produtos
def adicionar():
    print(" ________________________\n"
          "|  CADASTRO DE PRODUTOS  |\n"
          "|________________________|\n")

    nome = input("Nome: ")
    quantidade = input("Quantidade: ")

    produtos_salvos(
        nome,
        quantidade
    )

#remover itens da lista
def delete():

    try:

        id = int(input("ID para deletar: "))
        confirmar = input(f"Tem certeza que quer deletar o ID {id}? (s/n): ")
        if confirmar.lower() == "s":
            deletar_produto(id)
        else:
            print("Operação cancelada.")

    except ValueError:

        print("Digite apenas o ID em Números!")

#visualizar lista de produtos
def visualizar():
    produtos = listar_produtos()

    largura = 40

    borda     = "  +" + "-" * largura + "+"
    titulo    = "  |" + "LISTA DE PRODUTOS".center(largura) + "| "
    cabecalho = "  |" + f" {'ID':<5} {'NOME':<20} {'QTD':<10}" + "  |"

    print(borda)
    print(titulo)
    print(borda)
    print(cabecalho)
    print(borda)

    if not produtos:
        vazio = "  |" + "Nenhum produto cadastrado!".center(largura) + "|"
        print(vazio)
    else:
        for produto in produtos:
            id, nome, quantidade = produto
            linha = "  |" + f" {id:<5} {nome:<20} {quantidade:<10}" + "  |"
            print(linha)

    print(borda)
    time.sleep(2)

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
