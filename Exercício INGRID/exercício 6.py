def main ():
    total= float(input(f"Qual valor total da conta?: \t"))
    pessoas = int(input(f"Qual a quantidade de pessoas?: \t"))

    vlfinal = (total/pessoas)

    if vlfinal <= 50:
        print(f"total da conta foi: \t {total}")
        print(f"Valor por pessoa dentro do limite: \t {vlfinal}")
    else:
        print(f"total da conta foi: \t {total}")
        print(f"Valor por pessoa acima do limite: \t {vlfinal}")

if __name__ == "__main__":
    main()