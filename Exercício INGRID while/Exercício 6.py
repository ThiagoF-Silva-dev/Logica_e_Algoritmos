def main ():

    lista_produtos = []

    for produto in range(0,3):
        produto = str(input("Digite um produto:\t"))
        lista_produtos.append(produto)
    print(f"Produtos:{lista_produtos}\t")
    print()

    novo_produto = str(input("Digite um novo produto:\t"))
    lista_produtos.append(novo_produto)
    print(f"Lista de produtos atualizada:{lista_produtos}\t")
    print(f"Quantidade total de produtos: {len(lista_produtos)}")
    
if __name__=="__main__":
    main()