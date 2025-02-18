#solicitar um numero para treinar a tabuada
numSelec = int(input("digite um numero para treinar a tabuada: "))
acerto = 0
erro = 0
contador = 1
conta = 0
resposta = 0
#solicitar a resposta do calculo do numero multiplicado do 1 ao 10
for i in range (10):
  print("quanto é", numSelec, "x", contador, "?")
  resposta=int(input())
#A cada resposta você deverá validar e imprimir :”CORRETO” ou “QUE PENA, VOCÊ ERROU, O VALOR CORRETO É X “
  if resposta != (numSelec * contador):
    print("que pena, você errou, o valor correto é", numSelec * contador)
    erro += 1
  else:
    print("correto")
    acerto += 1
  contador += 1
#Ao final imprima “Total de acertos: y” e “Total de erros z”
print("total de acertos: ", acerto)
print("total de erros: ", erro)
