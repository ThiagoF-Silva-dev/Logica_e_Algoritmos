def main():

    convidados = ["Ana","Pedro","Maria","João","Lucas"]

    nome = str(input("Digite o nome do convidado que deseja remover:\t"))
    if nome in convidados:
        convidados.remove(nome)
        print("Convidado encontrado!\t")
    else:
        print("Convidado não encontrado!\t")
    print()
    convidados.pop()
    print(f"Convidados:{convidados}\t")

if __name__ == "__main__":
    main()