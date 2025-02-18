idadeGrupo = 0
idadeHomem = 0
IdadeMulher = 0
qtdH = 0
qtdM = 0
for i in range (10):
  idade = int(input("digite a idade: "))
  sexo = input("digite H para homem e M para mulher: ")

  if sexo == "H":
    idadeHomem += idade
    qtdH += 1
  elif sexo == "M":
    IdadeMulher += idade
    qtdM += 1

idadeGrupo = idadeHomem + IdadeMulher
mediaHomem = idadeHomem / qtdH
mediaMulher = IdadeMulher / qtdM
mediaGrupo = idadeGrupo / 10
print ()
print("a media do grupo é: ", mediaGrupo)
print("a media do homem é: ", mediaHomem)
print("a media da mulher é: ", mediaMulher)
