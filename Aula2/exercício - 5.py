def main ():

"""Exercício 5 — Aprovação do aluno"""

nota = float(input("Digite sua nota: \t "))
frequencia = int(input("Entre com a quantidade de dias com falta: \t"))

diasAula = 16
aulasTotais = diasAula * 4
aulasFaltadas = frequencia * 4
aulasPresentes = aulasTotais - aulasFaltadas
porcFreq = aulasPresentes / aulasTotais

if nota >= 6:

    if porcFreq >= 0.75:
        print("Nos vemos em 2027, você atingiu o mínimo de frequência e está aprovado! \t")
    else:
        print("Perdeu por frequência! Curse novamente a disciplina. \t")

else:
    print("Reprovado por nota. \t")


if __name__ == "__main__":
    main()