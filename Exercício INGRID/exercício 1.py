def main():
    Velocidade = int(input("Digite a velocidade do carro: \t"))

    if Velocidade > 80:
        print(f"Você foi multado por ecesso de velocidade! \t")
    else:
        print(f"Você não foi multado velocidade permitida! \t")

if __name__ == "__main__":
    main()