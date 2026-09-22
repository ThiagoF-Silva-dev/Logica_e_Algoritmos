def main ():
    vlcompra = float(input("Digite o valor total da compra: \t"))

    if vlcompra > 500:
        print(f"Compra negada limite 500 excedido! \t")
    else:
        print(f"Compra autorizada! \t")


if __name__ == "__main__":
    main()