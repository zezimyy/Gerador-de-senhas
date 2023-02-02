import random

letra = "abcdefghijklmnopqrstuvwxyz"
letraM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numero = "0123456789"
simbolo = "!@#"
senha = letra + numero + simbolo + letraM
tamanho = 16

while True:
  palavra_passe = "".join(random.sample(senha, tamanho))
  print(palavra_passe)
  print("")
  parar = input("deseja criar outra senha aleatoria? ")
  print("")
  if parar == 'n':
    break
  
  