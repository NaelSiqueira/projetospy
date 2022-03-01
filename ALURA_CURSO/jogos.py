import forca
import adivinhacao
from Udemy import loteria

print('######## Escolhe um jogo ########')

print('[1] forca [2] adivinhacao [3] loteria')

jogo = int(input('Qual o jogo ?'))

if (jogo == 1):
    print('Jogando forca')
    forca.jogar()
elif (jogo == 2):
    print('Jogando adivinhacao')
    adivinhacao.jogar()

elif (jogo == 3):
    print('Sorteando mega sena')
    loteria.jogar()

