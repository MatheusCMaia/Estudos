from random import randint
from time import sleep
jogador_numero = int(input('Digite um número entre 1 e 5: '))
numero_aleatorio = randint(1,5)
print('Processando...')
sleep(3)
if jogador_numero == numero_aleatorio:
    print('Parabéns você venceu!')
else:
    print('Que pena, você perdeu!')