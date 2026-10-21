def main():

    notas =[]

    for i in range(5):
        nota=float(input(f"Nota {i+1}: \t"))
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
    for i in range(len(notas)):
        print(f"Nota {notas[i]} -> Conceito {conceitos[i]}")


if __name__=="__main__":
    main()