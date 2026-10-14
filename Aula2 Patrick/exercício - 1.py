def main ():

"""Exercício 1 — Soma de dois números"""

    pc = float(input("Digite o peso da caixa: \t "))
    po = float(input("Digite o peso do objeto: \t "))
    cabe = pc-po
    print(f"O objeto cabe na caixa: \t ",pc>=po)


if __name__ == "__main__":
    main()