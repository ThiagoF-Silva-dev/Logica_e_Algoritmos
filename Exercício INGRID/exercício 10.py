def main ():
    numero = int(input("Digite um numero inteiro: \t "))

    resto = numero % 2

    if numero > 0:
        print(f"O Número {numero} é Positivo! \t")
        if resto == 0:
           print(f"O Número {numero} é PAR! \t")
        else:
            print(f"O Npumero {numero} é IMPAR \t")
    else:
        print(f"O Número {numeor} é Negativo! \t")


if __name__ == "__main__":
    main()