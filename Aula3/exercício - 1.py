def main():

"""Exercício 1 — Elegibilidade para Votação"""

 nascimento = int(input("Digite a sua data de nascimento: \t "))
 ano = int(input("Digite o ano atual: \t "))
 idade = ano-nascimento

 if idade <16:
 print(f"Vôce nao pode votar porque ainda e menor de idade! \t")
 else:
 print(f"Vôce está apto a votar por que ja tem a idade minima! \t")

if __name__ == "__main__":
    main()