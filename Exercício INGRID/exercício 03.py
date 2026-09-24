def main ():
    slatual = float(input("Digite o saldo atual: \t"))
    valorcomp = float(input("Digite o valor da compra: \t"))

    saldo = (slatual - valorcomp)

    if saldo > 0:
        print(f"Seu saldo continua possitivo: {saldo} \t")
    else:
        if saldo ==0:
            print(f"Saldo Zero! {saldo} \t")
        else:
            print(f"Saldo Negativo: {saldo} \t")


if __name__ == "__main__":
    main()