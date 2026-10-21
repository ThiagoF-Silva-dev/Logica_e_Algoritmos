def main ():
    temperaturas = []
    soma = 0
    contador_dias = 0

    for dia in range(1,8):
       temperatura = float(input(f"Temperatura do dia {dia}:\t"))
       temperaturas.append(temperatura)
    print(f"temperaturas: {temperaturas}")

    maior = temperaturas[0]
    menor = temperaturas[0]

    for temp in temperaturas:
       soma += temp

       if temp > maior:
         maior = temp

       if temp < menor:
         menor = temp

       if temp > 30:
         contador_dias += 1

    media = soma/7

    print(f"Temperatura média: {media}°C\t")
    print(f"Maior Temperatura: {maior}°C\t")
    print(f"Menor Temperatura: {menor}°C\t")
    print(f"Dias Acima de 30°C:{contador_dias}\t")





if __name__=="__main__":
    main()