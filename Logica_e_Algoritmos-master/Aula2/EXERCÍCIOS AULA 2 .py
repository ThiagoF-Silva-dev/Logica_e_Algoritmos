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

nota = float(input("Digite sua nota: \t"))
frequencia = int(input("Entre com a quantidade de dias com falta: \t"))
diasAula = 16
PorcFreq = ((frequencia*4)/(diasAula*4))

print(f"Sua nota é: \t {nota}")
print(f"Sua frequencia é: \t {PorcFreq}")

verificaNota = nota < 6
VerificaFreq = PorcFreq >=0.75

print(f"Reprovado por nota? \t", verificaNota)
print(f"Reprovado por falta?: \t",VerificaFreq)

if __name__ == "__main__":
    main()