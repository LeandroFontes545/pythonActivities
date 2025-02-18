login = str(input("digite seu login: "))
senha = str(input("digite sua senha: "))
contaCriada = False
while not contaCriada:
  if login != senha:
      contaCriada = True

  else:
    print("")
    print("login e senha iguais")
    print("")
    login = str(input("digite seu login: "))
    senha = str(input("digite sua senha: "))
print("")
print("Conta criada com sucesso!")
