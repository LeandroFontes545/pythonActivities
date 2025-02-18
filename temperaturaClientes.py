cliente = int(input("digite a quantidade de clientes: "))
somaTemp = 0
for valor in range (cliente):
  temp = float(input(f"qual a temperatura do cliente {valor + 1}: "))
  somaTemp += temp

  if temp <= 37.2:
    print (f"a temperatura {temp} é normal")
  elif  temp > 37.2 and temp <=38:
    print (f"a temperatura {temp} é considerado febril")
  elif temp > 38 and temp <=39:
    print (f"a temperatura {temp} é considerado febre")
  else:
    print (f"a temperatura {temp} é considerado superfebre")


media = somaTemp / cliente
print(" ")
print("a media de temperatura é:  %.2f" %(media))
print("a quantidade de pessoas é: ", cliente)
