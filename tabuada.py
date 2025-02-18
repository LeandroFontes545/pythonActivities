resposta = str(input("digite enter para saber a tabuada ou sair para encerrar ").upper())
contador = 1
resultado = 0
while resposta != "SAIR":
  multiplo = int(input("digite um numero para começar "))
  for i in range (10):
    resultado = multiplo * contador
    print(multiplo, " X ", contador, "=", resultado)
    contador += 1
  resposta = str(input("digite enter para saber a tabuada ou sair para encerrar ").upper())
  contador = 1
else:
  print(f"acabou")
