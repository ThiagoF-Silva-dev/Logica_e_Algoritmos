def main ():

"""Exercício 3 — Estoque da farmácia"""

    unidades = int(input("Digite o número de unidades vendidas: \t"))
    estoque = 100-unidades
    print(f"Estoque baixo?: \t",estoque<20)


if __name__ == "__main__":
    main()