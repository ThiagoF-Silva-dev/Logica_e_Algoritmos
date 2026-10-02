def main():
    dias = int(input("Digite há quantos dias a encomenda está aguardando retirada: \t"))

    if dias <= 2:
        print(f"Retirada sem Taxa! \t")
    elif dias >= 3 and dias <= 5:
        print(f"Cobrar taxa de R$ 5,00! \t")
    else:
        print(f"Retirada Bloqueada! \t")


if __name__ == "__main__":
    main()