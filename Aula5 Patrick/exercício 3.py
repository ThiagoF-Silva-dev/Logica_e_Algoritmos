def main ():

    """Soma acumulada"""

    numero = int(input("Digite um número: \t"))
    soma = 0
    while numero != 0:
        soma += numero
        numero = int(input("Digite um número: \t"))
    print(f"Soma Total: {soma}")


if __name__=="__main__":
    main()