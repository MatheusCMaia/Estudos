from time import sleep
from random import randint

rodadas = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {rodadas} -=-=-=')
for i in range(rodadas):
    valores = []
    while True:
        numeros = randint(0,100)
        if numeros not in valores:
            valores.append(numeros)
        if len(valores) == 6:
            break
    sleep(1)
    print(f'Jogo {i}: {valores}')
    print('-=-=-= BOA SORTE! -=-=-=')