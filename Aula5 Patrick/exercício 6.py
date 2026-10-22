def main ():
  numeros = []

  for numero in range(1,11):
      numero = int(input(f"Digite o {numero}º número: "))
      numeros.append(numero)

  print()

  pares = []
  impares = []

  for n in numeros:
     if n % 2 == 0 :
         pares.append(n)
     else:
         impares.append(n)

  print(f"Todos:{numeros}")
  print(f"Pares:{pares} ({len(pares)} números)")
  print(f"Ímpares:{impares} ({len(pares)} números)")






if __name__=="__main__":
    main()