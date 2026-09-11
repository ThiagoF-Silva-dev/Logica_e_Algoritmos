def main():

"""Exercício 6 — Validação de Usuário e Senha"""

    usuário = str(input(f"Digite o nome de usuário: \t"))
    senha = int(input(f"Digite a Senha: \t"))

    if usuário == "unisa" and senha == 1234:
        pergunta = input("Deseja acessar como Administrador? \t")
        if pergunta == "sim":
          print(f"Acesso Total! \t")
        else:
          print(f"Acesso Restrito! \t")
    elif usuário == "usuario" and senha == 5678:
          print(f"Acesso externo! \t")
    else:
       print(f"Usuário ou senha inválida!")



        """VERSAO 2"""

   usuário = str(input("Digite o nome de usuário: \t"))
   senha = int(input("Digite a senha: \t"))

   if usuário == "unisa" and senha == 1234:
      pergunta = input("Deseja acessar como Administrador? \t")
      if pergunta == "sim":
         print("Acesso Total! \t")
      else:
          print("Acesso Restrito! \t")
   else:
      if usuário == "usuario" and senha == 5678:
         print("Acesso Externo! \t")
      else:
         print("Usuário ou senha inválida!")

if __name__ == "__main__":
    main()
