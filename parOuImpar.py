numero = int(input("digite um numero ou 0 para sair \n"))
while numero != 0:
  if numero % 2 == 0:
    print(f"numero {numero} é par")
    numero = int(input("digite um numero ou 0 para sair \n"))
  else:
    print(f"numero {numero} é impar")
    numero = int(input("digite um numero ou 0 para sair \n"))
else:
  print(f"você saiu")
