numSelec = (input("digite um numero para treinar a tabuada: ").upper())
acerto = 0
erro = 0
contador = 1
resposta = 0
if numSelec != "SAIR":
  numSelec = int(numSelec)
while numSelec != "SAIR":
  print(f"quanto é {numSelec} x {contador} ? ou sair para encerrar \n")
  resposta = (input().upper())
  if resposta == "SAIR":
    numSelec = str(resposta.upper())
    print("total de acertos: ", acerto)
    print("total de erros: ", erro)
    break
  else:
    resposta = int(resposta)
  if resposta != (numSelec * contador) and resposta != str(resposta):
    print(f"que pena, você errou, o valor correto é {numSelec} * {contador}")
    erro += 1
  else:
    print("correto")
    acerto += 1
  contador += 1

else :
  print(f"total de acertos:  {acerto}")
  print(f"total de erros:  {erro}")
