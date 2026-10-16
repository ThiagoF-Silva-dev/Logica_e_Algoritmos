def main():

    """Classificação por idade"""

    idade = int(input("Digite a Sua idade e veja sua classificação: \t"))

    if idade >= 0 and idade <= 12:
        print(f"Criança!\t")
    elif idade >= 13 and idade <= 17:
        print(f"Adolecente!\t")
    elif idade >= 18 and idade <= 59:
        print(f"Adulto!\t")
    else:
        print(f"Idoso!\t")




if __name__ == "__main__":
    main()