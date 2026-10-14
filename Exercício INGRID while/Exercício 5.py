def main():
    palavra_chave = "python123"

    senha = str(input("Digite a palavra Chave:\t"))

    while senha != palavra_chave:
        print(f"Palavra Chave errada digite novamente!\t")
        senha = str(input("Digite a palavra Chave: \t"))
    print(f"Acesso Liberado!")

if __name__ == "__main__":
    main()