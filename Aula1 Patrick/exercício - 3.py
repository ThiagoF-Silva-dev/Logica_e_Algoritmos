def main ():
"""3-Retângulo
   #Faça um algoritmo que leia a base e a altura de um retângulo e calcule sua área."""

 base = float(input("Digite o valor da base do retângulo:\t"))
 altura = float(input("Digite o valor da altura do retângulo:\t"))
 area = base*altura
 print(f"A área do retângulo é:\t {area}")

if __name__ == ("__main__"):
    main()