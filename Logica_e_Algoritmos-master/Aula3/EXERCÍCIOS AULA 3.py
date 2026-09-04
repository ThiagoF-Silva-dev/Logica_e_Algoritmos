def main():

   """Exercício 1 — Elegibilidade para Votação"""

    #nascimento = int(input("Digite a sua data de nascimento: \t "))
    #ano = int(input("Digite o ano atual: \t "))
    #idade = ano-nascimento

    #if idade <16:
        #print(f"Vôce nao pode votar porque ainda e menor de idade! \t")
    #else:
        #print(f"Vôce está apto a votar por que ja tem a idade minima! \t")

   """Exercício 2 — Número Positivo ou Negativo"""

   #numero= int(input("Digite um número: \t"))

   #if numero >=0:
       #print(f"O numero é Positivo! \t")
   #else:
       #print(f"O número é Negativo! \t")

   """Exercício 3 — Carteira de Motorista"""

   #idade = int(input(f"Digite sua idade: \t"))

   #if idade>= 18:
     #cnh = input(f"Vôce, possui CNH (s/n): \t")
     #if cnh == "s":
          #print(f"Vôce, pode dirigir! \t")
     #else:
          #print(f"Vôce, Precisa tirar a carteira! \t")
   #else:
     #print(f"Vôce, não pode dirigir! \t")

   """Exercício 4 — Positivo,Negativo, Zero, par ou impar"""

   numero = int(input("Digite um numero inteiro: \t"))

   if numero % 2 == 0:
       print(f"É par!")
   else:
       print(f"É ímpar!")



if __name__ == "__main__":
    main()