import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1)Jogo da Forca (2)Jogo de Adivinhação")

jogo = int(input("Escolha o jogo: "))

if (jogo == 1):
    print("Jogando Jogo da Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Jogo da Adivinhação")
    adivinhacao.jogar()
