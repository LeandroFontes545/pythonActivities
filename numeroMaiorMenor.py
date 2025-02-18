valor = 0
numero = []
aux = []

for valor in range (1, 11):
  numeroEscolhido = int(input("digite um numero: "))
  numero.append(numeroEscolhido)
media = sum(numero) / 10

print("o maior número é o ", max(numero))
print("o menor número é o ", min(numero))
print("media ", media)
