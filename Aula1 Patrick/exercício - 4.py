def main ():
"""4-Conversão de temperaturas
  Faça um algoritmo que leia uma temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = (C × 1,8) + 32"""

 celsius = float(input("Digite a temperatura em Celsius:\t"))
 Fahrenheit = (celsius * 1.8)+32
 print(f"A temperatura convertida para Fahrenheit é de:\t{Fahrenheit}")

if __name__ == ("__main__"):
    main()