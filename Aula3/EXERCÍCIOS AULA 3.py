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

   # idade = int(input(f"Digite sua idade: \t"))
   #
   # if idade>= 18:
   #    cnh = input(f"Vôce, possui CNH (s/n): \t")
   #    if cnh == "s":
   #        print(f"Vôce, pode dirigir! \t")
   #    else:
   #        print(f"Vôce, Precisa tirar a carteira! \t")
   # else:
   #    print(f"Vôce, não pode dirigir! \t")

   """Exercício 4 — Positivo, Negativo, Zero, Par ou Ímpar"""

   # numeInt = int(input("Digite um número inteiro: \t "))
   #
   # resto = numeInt % 2
   #
   # if numeInt > 0:
   #     print(f"É Positivo! \t")
   #     if (resto == 0):
   #          print(f"É PAR \t ")
   #     else:
   #          print(f"É IMPAR \t ")
   # else:
   #     if numeInt < 0:
   #         print(f"Número Negativo! \t ")
   #     else:
   #         print(f"Zero não é positivo nem negativo! ")

   """Exercício 5 — Par/Ímpar e Comparação de Dois Números"""
   #
   # numero = int(input("Digite um numero inteiro: \t"))
   #
   # resto = numero % 2
   #
   # if (resto == 0):
   #     print(f"É PAR! \t")
   # else:
   #     print(f"É IMPAR! \t")
   #
   # print ("_"*30)
   #
   # n1= int(input("Digite o 1° número: \t"))
   # n2 = int(input("Digite o 2° número: \t"))
   #
   # if n1 > n2:
   #     print(f"{n1} é maior que {n2} \t ")
   # else:
   #     if n2 > n1:
   #         print(str(n2)+" É maior que"+str(n1))
   #     else:
   #         print(str(n1)+" É igual a "+str(n1))


   """Exercício 6 — Validação de Usuário e Senha"""

   # usuário = str(input(f"Digite o nome de usuário: \t"))
   # senha = int(input(f"Digite a Senha: \t"))
   #
   # if usuário == "unisa" and senha == 1234:
   #     pergunta = input("Deseja acessar como Administrador? \t")
   #     if pergunta == "sim":
   #       print(f"Acesso Total! \t")
   #     else:
   #       print(f"Acesso Restrito! \t")
   # elif usuário == "usuario" and senha == 5678:
   #       print(f"Acesso externo! \t")
   # else:
   #    print(f"Usuário ou senha inválida!")

       # """VERSAO 2"""

   usuário = str(input("Digite o nome de usuário: \t"))
   senha = int(input("Digite a senha: \t"))

   if usuário == "unisa" and senha == 1234:
      pergunta = input("Deseja acessar como Administrador? \t")
      if pergunta == "sim":
         print("Acesso Total! \t")
      else:
          print("Acesso Restrito! \t")
   else:
      if usuário == "usuario" and senha == 5678:
         print("Acesso Externo! \t")
      else:
         print("Usuário ou senha inválida!")




if __name__ == "__main__":
    main()