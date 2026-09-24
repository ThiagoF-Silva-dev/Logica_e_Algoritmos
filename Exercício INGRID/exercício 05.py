def main():
    produto1 = float(input(f"Digite o valor do primeiro produto: \t "))
    produto2 = float(input(f"Digite o valor do segundo produto: \t "))

    valor = (produto1 + produto2)

    if valor >= 150:
        print(f"Você ganhou frete gratis! \t")
    else:
        print(f"Frete pago pelo cliente! \t")


if __name__ == "__main__":
    main()