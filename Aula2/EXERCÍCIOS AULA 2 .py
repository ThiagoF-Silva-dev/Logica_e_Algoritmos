def main ():
 """Exercício 1 — Soma de dois números"""

    #pc = float(input("Digite o peso da caixa: \t "))
    #po = float(input("Digite o peso do objeto: \t "))
    #cabe = pc-po
    #print(f"O objeto cabe na caixa: \t ",pc>=po)

"""Exercício 2 — Limite de peso de uma caixa"""

    #numero1 = float(input("Digite o valor do primeiro numéro: \t"))
    #numero2 = float(input("Digite o valor do segundo numéro: \t"))
    #valor = numero1+numero2
    #print(f"A soma dos dois numéros e maior que 20? \t", valor >=20)

"""Exercício 3 — Estoque da farmácia"""

    #unidades = int(input("Digite o número de unidades vendidas: \t"))
    #estoque = 100-unidades
    #print(f"Estoque baixo?: \t",estoque<20)

"""Exercício 4 — Controle de velocidade"""

   #velocidade = int(input("Qual a Velocidade do carro?: \t"))
   #print(f"O carro foi multado? \t",velocidade>80)

"""Exercício 5 — Aprovação do aluno"""

nota = float(input("Digite sua nota: \t "))
frequencia = int(input("Entre com a quantidade de dias com falta: \t"))

diasAula = 16

# Cada dia tem 4 aulas. Calculamos a porcentagem de PRESENÇA subtraindo as faltas:
aulasTotais = diasAula * 4
aulasFaltadas = frequencia * 4
aulasPresentes = aulasTotais - aulasFaltadas

porcFreq = aulasPresentes / aulasTotais

# 1. Primeiro testamos se a nota é suficiente
if nota >= 6:
    # 2. Se a nota for boa, testamos se a frequência ATINGE o mínimo (75% ou 0.75)
    if porcFreq >= 0.75:
        print("Nos vemos em 2027, você atingiu o mínimo de frequência e está aprovado! \t")
    else:
        print("Perdeu por frequência! Curse novamente a disciplina. \t")

else:
    print("Reprovado por nota. \t")




if __name__ == "__main__":
    main()