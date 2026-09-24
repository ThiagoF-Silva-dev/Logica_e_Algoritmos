def main():
    manha = int(input(f"Digite a quantidade vendida no periodo da manhã: \t "))
    tarde = int(input(f"Digite a quantidade vendida no periodo da tarde: \t "))

    total = (manha + tarde)

    if total >= 100:
        print(f"meta diaria atingida! \t ")

    else:
        print(f"meta diaria não atingida! \t ")


if __name__ == "__main__":
    main()