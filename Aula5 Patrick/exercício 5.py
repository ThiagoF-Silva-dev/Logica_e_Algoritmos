def main():

    """Notas e conceitos"""

   alunos = ["Bruno","Thiago","Ana","Amanda","Julia"]
   notas = []

   for i in range(5):

       nota = float(input(f"Nota do {alunos[i]}: \t"))
       notas.append(nota)

       conceitos = []

   for nota in notas:
       if nota < 50:
           conceitos.append("D")
       elif nota < 70:
           conceitos.append("C")
       elif nota < 90:
           conceitos.append("B")
       else:
           conceitos.append("A")

   for i in range(len(alunos)):
       print(f"{alunos[i]} -> Nota {notas[i]} -> Conceito {conceitos[i]}")


if __name__=="__main__":
    main()