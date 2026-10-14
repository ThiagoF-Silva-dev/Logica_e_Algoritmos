def main ():
"""5-Salário
   Faça um algoritmo que leia a quantidade de horas trabalhadas e o valor pago por hora, e calcule o salário final."""

 horas = int(input("Digite o total de horas trabalhadas:\t"))
 valor = float(input("Digite o valor pago por hora trabalhada:\t"))
 salario = horas*valor
 print(f"O salário final de acordo com seus ganhos será de:\t{salario}")

if __name__ == ("__main__"):
    main()