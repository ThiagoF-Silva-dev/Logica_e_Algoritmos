def main ():
    ar = int(input("Concentração de dióxido de carbono, em partes por milhão: \t"))

    if ar <= 0:
        print("Invalido \t")
    elif ar <= 800:
        print("Ar Adequado! \t")
    elif ar > 800 and ar <= 1200:
        print("Atenção! \t")
    else:
        print("Ventilar a sala")


if __name__ == "__main__":
     main()