def main ():

    """Conversão de nota para conceito"""

    nota = int(input("Digite a nota para ver o conceito:\t"))

    if nota < 0:
        print(f"Valor Invalido!\t")
    elif nota <= 49:
        print(f"Conceito D! \t")
    elif nota <= 69:
        print(f"Conceito C! \t")
    elif nota <= 89:
        print(f"Conceito B! \t")
    elif nota <= 100:
        print(f"Conceito A! \t")
    else:
        print(f"Valor Invalido! \t")


if __name__ == "__main__":
    main()