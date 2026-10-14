def main():

"""Exercício 4 — Positivo, Negativo, Zero, Par ou Ímpar"""

    numeInt = int(input("Digite um número inteiro: \t "))

    resto = numeInt % 2

    if numeInt > 0:
        print(f"É Positivo! \t")
        if (resto == 0):
             print(f"É PAR \t ")
        else:
             print(f"É IMPAR \t ")
    else:
        if numeInt < 0:
            print(f"Número Negativo! \t ")
        else:
            print(f"Zero não é positivo nem negativo! ")

if __name__ == "__main__":
    main()