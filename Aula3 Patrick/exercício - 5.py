def main():

"""Exercício 5 — Par/Ímpar e Comparação de Dois Números"""

    numero = int(input("Digite um numero inteiro: \t"))

    resto = numero % 2

    if (resto == 0):
        print(f"É PAR! \t")
    else:
        print(f"É IMPAR! \t")

    print ("_"*30)

    n1= int(input("Digite o 1° número: \t"))
    n2 = int(input("Digite o 2° número: \t"))

    if n1 > n2:
        print(f"{n1} é maior que {n2} \t ")
    else:
        if n2 > n1:
            print(str(n2)+" É maior que"+str(n1))
        else:
            print(str(n1)+" É igual a "+str(n1))

if __name__ == "__main__":
    main()