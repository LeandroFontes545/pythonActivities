resposta = str(input("voce gosta de python ").upper())
while resposta != "SIM" and resposta != "S":
    print(f"resposta errada")
    resposta = str(input("voce gosta de python ").upper())
else:
  print(f"resposta certa")
