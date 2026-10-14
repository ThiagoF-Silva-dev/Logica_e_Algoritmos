def main ():
    contagem = int(input("Digite um número inteiro para o lançamento do foguete: \t"))

    print(f"Contagem regressiva para o lançamento! \t")

    while 0 <= contagem:
        print(contagem)
        contagem = contagem - 1
    print(f"Foguete Lançado!")




if __name__ == "__main__":
    main()