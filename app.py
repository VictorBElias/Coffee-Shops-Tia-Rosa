lista_de_salgados = {
    "coxinha" : 9,
    "pastel" : 5,
    "bauru" : 5,
    "pao com carne de sol" : 15,
    "empada" : 6
}


lista_de_bebidas = {
    "coca-cola" : 3.5,
    "agua com gas" : 3,
    "guarana" : 3.5,
    "suco de laranja" : 5,
    "suco de caja" : 5
}

clientes = []

def escreverDespedida():
    print("Encerrado")

def fazerPedido(clientes, lista_de_bebidas, lista_de_salgados):
    while True:
        resposta = input("Você quer cadastrar novo cliente? Sim ou Não?\n").lower()
        if resposta == "sim":
            cliente = input("Qual o nome do cliente?\n")
            clientes.append(cliente)
        else:
            break

    print("Clientes cadastrados:", clientes)

    valor_total = []

        
    while True:
        print(f"\nO que o sr(a). {cliente} deseja?")
        print("[1]Salgados")
        print("[2]Bebidas")
        print("[3]Valor final")
        print("[4]Sair")

        desejo = input()
        
        if desejo == "1":
            lista_nome_salgados = list(lista_de_salgados.keys())
            print("Salgados disponíveis:", lista_nome_salgados)
            while True:
                escolha = input("Digite o nome do produto desejado (ou 'sair' para voltar ao menu): ").lower()
                if escolha == "sair":
                    break
                elif escolha in lista_de_salgados:
                    preco = lista_de_salgados[escolha]
                    valor_total.append(preco)
                    print(f"O preço da {escolha} e R$ {preco:.2f}")
                else:
                    print("Produto não encontrado")
                
                
        elif desejo == "2":
            lista_nome_bebidas = list(lista_de_bebidas.keys())
            print("Bebidas disponíveis:", lista_nome_bebidas)
            while True:
                escolha = input("Digite o nome da bebida desejada (ou 'sair' para voltar ao menu): ").lower()
                if escolha == "sair":
                    break
                elif escolha in lista_de_bebidas:
                    preco = lista_de_bebidas[escolha]
                    valor_total.append(preco)
                    print(f"O preço da {escolha} e R$ {preco:.2f}\nAlguma bebida a mais? ")
                else:
                    print("Produto não encontrado")

        elif desejo == "3":
            soma = sum(valor_total)
            print(f"\n\tO preço final é {soma:.2f}")
            break

        else:
            break
    
    escreverDespedida()

if __name__ == "__main__":
    print("BEM VINDO AO COFFE SHOPS TIA ROSA")
    fazerPedido(clientes, lista_de_bebidas, lista_de_salgados)
