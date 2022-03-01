import random



QUADRANTE_1 = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
QUADRANTE_2 = [6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 26, 27, 28, 29, 30]
QUADRANTE_3 = [31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]
QUADRANTE_4 = [36, 37, 38, 39, 40, 46, 47, 48, 49, 50, 56, 57, 58, 59, 60]


TOTAL_JOGOS = 10


def gerar_dezenas():
    dezenas = []

    sorteio = random.sample(set(QUADRANTE_1), 2)
    for numero in sorteio:
        dezenas.append(numero)

    sorteio = random.sample(set(QUADRANTE_2), 2)
    for numero in sorteio:
        dezenas.append(numero)

    sorteio = random.sample(set(QUADRANTE_3), 2)
    for numero in sorteio:
        dezenas.append(numero)

    sorteio = random.sample(set(QUADRANTE_4), 2)
    for numero in sorteio:
        dezenas.append(numero)


    dezenas = random.sample(set(dezenas), 6)
    dezenas = sorted(dezenas)
    dezenas = [str(dez) for dez in dezenas]

    return ' '.join(dezenas)


meus_jogos = []


for x in range(0, TOTAL_JOGOS):
    meus_jogos.append(gerar_dezenas())


meus_jogos = list(dict.fromkeys(meus_jogos))


for jogo in meus_jogos:
    print(jogo)

##if(__name__=='__main__'):
 ##   jogar()