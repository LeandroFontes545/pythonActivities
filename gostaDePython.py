resposta = ""
while True:
  resposta = str(input("voce gosta de python ").upper())
  if resposta != "SIM":
    print(f"resposta errada")
  else:
    print(f"resposta certa")
    break
