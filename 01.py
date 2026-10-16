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
            print(produto)

def saida():
    sa = input("Digite o nome do produto que quer retirar ao estoque: ")
    quan = int(input("Digite a quantidade produtos que deseja retirar no estoque: "))
    for produto in produtos:
        if produto["nome"] == sa:
            produto["estoque"] -= quan
            print(produto)



  
           
def remover():
    re = input("Digite o nome do produto que deseja remover do sistema:  ")
    for produto in produtos:
        if produto["nome"] == re:
            produtos.remove(produto)
            break
    print(produtos) 


def adicionar():
    print(produtos[-1])
    id = produtos[-1]["id"]          
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do seu produto: ") 
    preco = int(input("Digite o preço do seu produto: ")) 
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
    print(novo_produto) 







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
       criar()

   elif opcao == "6":
    remover()   

   elif opcao == "7":
       adicionar()

   elif opcao == "0":
    print("Saindo do sistema...")
    break
  
   else:
       print("Opção inválida, tente novamente!!!") 