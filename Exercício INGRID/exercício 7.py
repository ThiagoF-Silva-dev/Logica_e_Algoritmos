def main ():
    base = float(input("Digite o valor da base: \t"))
    expoente = float(input("Digite o valor do expoente: \t"))

    resultado = base ** expoente

    if resultado > 100:
        print(f"O resultado da potencia e maior que 100: {resultado} \t")
    else:
        print(f"O resultado da potencia e menor que 100: {resultado} \t")

if __name__ == "__main__":
    main()