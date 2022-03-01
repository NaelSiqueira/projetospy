import random

def jogar():

    print('Bem vindo ao jogo de adivinhação')

    numero_secreto= random.randrange(1,101)
    total_tentativa=0
    rodada=1
    print(numero_secreto)

    print('Qual o nivel de dificuldade?')
    print('[1]facil, [2]medio, [3]dificio')
    nivel=int(input('Coloque aqui um nivel almejado: '))

    if(nivel==1):
        total_tentativa=20
    elif(nivel==2):
        total_tentativa=10
    else :
        total_tentativa=5
    for rodada in range(1,total_tentativa, +1):
        print("tentativa {} de {}". format(rodada,total_tentativa))
        chute = int(input("Digite o seu numero entre 1 e 100:  "))
        print('Você digitou', chute)

        if(chute<1 or chute>100):
            print('Você deve digiter um numero entre 1 e 100')
            continue


        acertou= numero_secreto == chute
        maior=chute>numero_secreto
        menor=chute<numero_secreto1


        if (acertou):
            print ('você acertou')
            break
        else:
            if(maior):
                print('Você errou, o numero foi maior que o secreto')
            elif(menor):
                print('Você errou, o numero foi menor que o secreto')




    print('fim do jogo')

if(__name__=='__main__'):
    jogar()



