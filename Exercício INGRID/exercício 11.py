def main ():

  numero = int(input("Digite um número inteiro: \t"))

  if (numero >= 10) and (numero <= 100) and (numero % 5 ==0):
      print(f"O número {numero} atende às duas condições (está entre 10 e 100 e é divisível por 5)! \t")
  else:
      print(f"O número {numero} não atende às duas condições! \t")

if __name__ == "__main__":
    main()