def main():
    atraso = int(input(f"Qual o tempo de atraso do pedido?: \t"))

    if atraso <= 10:
        print(f"Nenhum crédito! \t")
    elif atraso <= 25:
        print(f"Você vai receber R$ 5,00 de crédito! \t")
    elif atraso <= 45:
        print(f"Você vai receber R$ 10,00 de crédito! \t")
    else:
        print(f"Você vai recever R$ 20,00 de crédito! \t")


if __name__ == "__main__":
    main()