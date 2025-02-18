senha = str(input("Digite a senha para continuar ou sair para encerrar \n"))
while senha != "1234":
  print(f"senha incorreta, tente novamente \n")
  senha = str(input("Digite a senha para continuar ou sair para encerrar \n"))
  if senha.upper() == "SAIR":
    print("Saindo...")
    break
