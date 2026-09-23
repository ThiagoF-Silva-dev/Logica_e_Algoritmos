def main ():
    numero = int(input("Digite um número inteiro: \t"))
    divisão = (numero // 7)
    resto = numero % 7

    if resto == 0:
        print(f"O resultado da divisão é: \t {divisão}")
        print(f"O número é divisível por 7!")
    else:
        print(f"O resultado da divisão é: \t {divisão}")
        print(f"Resto da divisão: \t {resto}")
        print(f"O número não e divisível por 7!")


if __name__ == "__main__":
    main()