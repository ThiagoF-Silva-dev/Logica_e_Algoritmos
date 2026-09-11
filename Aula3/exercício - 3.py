def main():

"""Exercício 3 — Carteira de Motorista"""

    idade = int(input(f"Digite sua idade: \t"))

    if idade>= 18:
       cnh = input(f"Vôce, possui CNH (s/n): \t")
       if cnh == "s":
           print(f"Vôce, pode dirigir! \t")
       else:
           print(f"Vôce, Precisa tirar a carteira! \t")
    else:
       print(f"Vôce, não pode dirigir! \t")

if __name__ == "__main__":
    main()