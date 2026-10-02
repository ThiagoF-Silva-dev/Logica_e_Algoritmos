def main():
    candidato = str(input("Digite a situação do candidato: \t"))

    if candidato == "deferida":
        print(f"Candidatura aprovada")
    elif candidato == "pendente":
        print(f"Candidatura aguardando análise")
    elif candidato == "indeferida":
        print(f"Candidatura não aprovada")
    else:
        print(f"Situação inválida")

if __name__ == "__main__":
     main()