def main():

    """Tabuada"""

    numero = int(input("Digite um número inteiro para ver a tabuada completa: \t"))
    contador = 0
    while contador <= 10:
        resultado = contador * numero
        print(f"{numero}x{contador}={resultado}")
        contador = contador + 1

if __name__ == "__main__":
    main()