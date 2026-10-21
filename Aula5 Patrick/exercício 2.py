def main ():

    """Pares"""

     print(f"Calculando a soma dos 50 primeiros números pares (de 2 a 100)...\t")
     soma = 0
     contador = 2

     while contador <= 100:
         soma += contador
         contador += 2
     print(f"A soma total com while é: {soma} \t")


     print(f"Calculando a soma dos 50 primeiros número pares (de 2 a 100)...\t")

     soma = 0
     for i in range(2, 101, 2):
         soma += i
     print(f"A soma total com for é: {soma} \t ")





if __name__ == "__main__":
    main()