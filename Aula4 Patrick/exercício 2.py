def main():

    """Preço do ingresso do cinema"""

    idade = int(input("Digite a idade para ver o valor do ingresso do cinema:\n"))

    if idade <= 12:
        print(f"Valor do ingresso R$: 10,00 Reais!\t")
        print(f"Até 12 anos!\t")

    elif idade >= 13 and idade <= 17:
        print(f"Valor do ingresso R$: 15,00 Reais!\t")
        print(f"Idade entre 13 e 17 anos!\t")

    elif idade >= 18 and idade <= 59:
        print(f"Valor do ingresso R$: 20,00 Reais!\t")
        print(f"Idade entre 18 e 59 anos!\t")
    else:
        print(f"Valor do ingresso R$: 12,00 Reais!\t")
        print(f"Idade 60 anos ou mais!\t")

if __name__ == "__main__":
    main()