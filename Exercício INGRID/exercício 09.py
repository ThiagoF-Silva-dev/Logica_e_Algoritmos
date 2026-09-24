def main ():
    alunos = int(input("Qual a quantidade de alunos da turma: \t"))
    grupos = (alunos // 4)
    sobrou = (alunos % 4)

    print(f"Foram formados {grupos} Grupos completos \t")
    print(f"{sobrou} Alunos sem grupos \t")

    if grupos >= 5 and sobrou == 0:
        print(f"Foi possível formar {grupos} Grupos e não sobrou nenhum aluno! \t")
    else:
        print(f"Não foi possível atingir a meta (mínimo de 5 grupos completos sem sobras).")





if __name__ == "__main__":
    main()