import time

estoque = []

while True:

    time.sleep(1)

    print("" \
    "    _____________________________\n"
    "   |   GERENCIADOR DE ARQUIVOS   |\n"  \
    "   |_____________________________|\n"
    "   |                             |\n"
    "   |   [1] ADICIONAR PRODUTO     | \n" \
    "   |   [2] DELETAR PRODUTO       | \n" \
    "   |   [3] VISUALIZAR PRODUTO    |\n"
    "   |   [4] SAIR                  |\n"
    "   |_____________________________|\n")

    time.sleep(1)
    
    inicio = input("Digite o numero da opção que você quer selecionar: ")

    if inicio != "1" and inicio != "2" and inicio != "3" and inicio != "4":
        print("OPÇÃO INVALIDA...")
        continue
    
    #adicionar produtos

    else:
        if inicio == "1":
            print(" ________________________\n"
                 "|  CADASTRO DE PRODUTOS  |\n"
                 "|________________________|\n")
                 
            itens = int(input("Quantos itens você deseja cadastrar? "))

            for i in range(itens):
                estoque.append(input("\nColoque o produto que deseja:\n"))
            print("\nCADASTRO CONCLUIDO...")
            time.sleep(1)

# remover os produtos

        if inicio == "2":
            
            while True:
                print("| REMOVER ITEM |")
                remover = input("Digite o produto que você quer remover: ")
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

#visualizar produtos

        if inicio == "3":
            print("| VISUALIZAR ITEM |")
            print("seu estoque no momento é: ", estoque)
            time.sleep(3)

#sair do programa

        if inicio == "4":
            time.sleep(1)
            print("|  ESPERO QUE TENHA GOSTADO DO PROTÓTIPO,  | \n" \
                  "|  ATÉ A PROXIMA                           |")
            time.sleep(1)
            break

