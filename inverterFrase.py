#um programa em Python que receba uma string do usuário e mostre de trás para frente.
frase = input("digite uma frase: ")
totalChar = len(frase)
# len(frase) faz com que enumere cada posição de letra
posicao = totalChar -1
# -1 faz com que leia a letra do final
fraseInversa = ""
for i in range (totalChar):
# toda vez que o i passar pelo comprimento do totalChar
  fraseInversa += frase[posicao]
# a frase inversa recebe a letra correspondente a posição - posição
  posicao -= 1
print(fraseInversa)
