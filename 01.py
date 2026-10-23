import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding = "utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding = "utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def listar():
    print(produtos)

def buscar():
    busc = input("Digite o nome do produto que vocên deseja: ")
    for produto in produtos:
        if produto["nome"] == busc:
            print(produto)

def entrada():
    en = input("Digite o nome do produto que quer adicionar ao estoque: ")
    quan = int(input("Digite a quantidade produtos que deseja colocar no estoque: "))
    for produto in produtos:
        if produto["nome"] == en:
            produto["estoque"] += quan
            salvar_produtos(produtos)
            print(produto)

def saida():
    sa = input("Digite o nome do produto que quer retirar ao estoque: ")
    quan = int(input("Digite a quantidade produtos que deseja retirar no estoque: "))
    for produto in produtos:
        if produto["nome"] == sa:
            produto["estoque"] -= quan
            salvar_produtos(produtos)
            print(produto)


def alterar():
    nome = input("Digite o nome do produto que deseja fazer alterações: ")

    for produto in produtos:
        if produto["nome"] == nome:

            print("1 - Alterar nome")
            print("2 - Alterar preço")
            print("3 - Alterar categoria")
            print("4 - Alterar id")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                novo_nome = input("Digite o novo nome: ")
                produto["nome"] = novo_nome

            elif opcao == "2":
                novo_preco = float(input("Digite o novo preço: "))
                produto["preco"] = novo_preco

            elif opcao == "3":
                nova_categoria = input("Digite a nova categoria: ")
                produto["categoria"] = nova_categoria

            elif opcao == "4":
                novo_id = int(input("Digite o novo id: "))
                produto["id"] = novo_id

            else:
                print("Opção inválida")
                return

            salvar_produtos(produtos)

            print(produto)
            return

    print("Produto não encontrado.")


  
           
def remover():
    re = input("Digite o nome do produto que deseja remover do sistema:  ")
    for produto in produtos:
        if produto["nome"] == re:
            produtos.remove(produto)
            break
        salvar_produtos(produtos)
    print(produtos) 


def adicionar():
    id = produtos[-1]["id"]          
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do seu produto: ") 
    preco = float(input("Digite o preço do seu produto: ")) 
    estoque = int(input("Digite a quantidade do estoque: "))
    id += 1 

    novo_produto = {
        "id": id,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    }   

    produtos.append(novo_produto)
    salvar_produtos(produtos)  
    print(novo_produto) 


def baixo():
    for produto in produtos:
        if produto["estoque"] <= 10:
            print(produto)







produtos = carregar_produtos()






while True: 
   print("Controle de Estoque")
   print("1 - Listar os produtos")
   print("2 - Buscar por produto")
   print("3 - Entrada no estoque")
   print("4 - Saida no estoque")
   print("5 - Alterar informações do produto")
   print("6 - Remover produto")
   print("7 - Adicionar produto")
   print("8 - Estoque baixo")
   print("0 - sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
    listar()

   elif opcao == "2":
    buscar()
 
   elif opcao == "3":
    entrada()

   elif opcao == "4":
    saida()

   elif opcao == "5":
    alterar()

   elif opcao == "6":
    remover()   

   elif opcao == "7":
       adicionar()

   elif opcao == "8":
       baixo()     

   elif opcao == "0":
    print("Saindo do sistema...")
    break
  
   else:
       print("Opção inválida, tente novamente!!!") 