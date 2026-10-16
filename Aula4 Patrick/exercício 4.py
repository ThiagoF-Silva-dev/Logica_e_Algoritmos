def main():

    """Classificação da temperatura"""

    temperatura = float(input("Digite a Temperatura atual em Celsius: \t"))

    if temperatura <= 10:
        print(f"{temperatura}°C Muito Frio!\t")
    elif temperatura <= 20:
        print(f"{temperatura}°C Frio!\t")
    elif temperatura <= 30:
        print(f"{temperatura}°C Agradável!\t")
    elif temperatura <= 35:
        print(f"{temperatura}°C Calor!\t")
    else:
        print(f"{temperatura}°C Muito Calor!\t")


if __name__ == "__main__":
    main()