notas = 0
qnt_notas_info = 0
while True:
  nota = float(input("informe a nota (-1 para finalizar): "))
  if (nota == -1):
    break
  notas += nota
  qnt_notas_info += +1
if qnt_notas_info > 0:
  media = notas / qnt_notas_info
  print(f"Quantidade de notas informadas: {qnt_notas_info}")
  print(f"Média: {media:.2f}")
else:
  print("nenhuma nota informada")
