def main():

    """Situação do Aluno"""

    media = float(input("Digite a média do aluno: \t"))
    faltas = int(input("Digite a quantidade de faltas: \t"))

    if media < 0 or media > 10:
        print(f"Média invalida!")

    if faltas < 0 or faltas > 100:
        print(f"Quantidade invalida!")

    if media >= 7:
        if faltas < 25:
            print(f"Aprovado!")
        else:
            print("Reprovado por Falta!")
    else:
        print("Reprovado por nota")
if __name__ == "__main__":
    main()