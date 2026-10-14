def main ():
    numero = int(input("Digite um numero inteiro Positivo: \t"))
    contador = 0

    for i in range(1, numero + 1):
      if i % 2 == 0:
          contador = contador + 1
          print(f"Esses são os números pares: {i}\n")
    print(f"Total de numeros pares: {contador} \t")


if __name__ == "__main__":
    main()