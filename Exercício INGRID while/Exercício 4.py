def main():
  print("="*25)
  print()
  print("LISTA DE PRODUTOS ESTOQUE")
  print()
  print("="*25)

  estoque = [12, 0, 8, 0, 15]

  for i in estoque:
     if i == 0:
         print(f"Produto Esgotado! \n")
     else:
         print(f"Tem {i} em estoque! \n")


if __name__ == "__main__":
    main()