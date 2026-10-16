def main():

    """Classificação da velocidade da internet"""

    internet= float(input("Qual a Velocidade da internet: \t"))

    if internet <= 10:
        print(f"{internet} Mbps Velocidade Lenta!\t")
    elif internet <= 50:
        print(f"{internet} Mbps Velocidade Média!\t")
    elif internet <= 200:
        print(f"{internet} Mbps Velocidade Rápida!\t")
    else:
        print(f"{internet} Mbps Velocidade Ultra Rápida!\t")


if __name__ == "__main__":
    main()