from random import randint
from time import sleep
pontos_jogador = 0
pontos_computador = 0
while True:
    print('''

=======================
= JOGO DA ADIVINHAÇÃO =
=======================


1 - Jogar
2 - Mostrar placar
3 - Resetar placar
4 - Encerrar

''')
    print('')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        print('O computador está pensando...')
        sleep(2)
        print('O computador pensou em número!')
        jogador_numero = int(input('Digite um número de 1 a 3: '))
        computador_numero = randint(1,3)
        if jogador_numero == computador_numero:
            pontos_jogador += 1
            print('Parabéns você acertou no número que o computador pensou!')
            print('Você ganhou 1 ponto!')
        else:
            pontos_computador += 1
            print(f'O computador pensou no número: {computador_numero}')
            print('Que pena, você pensou em um número totalmente diferente!')
            print('Computador ganhou 1 ponto!')
    elif opcao == 2:
        print(f'O placar atual está: Computador {pontos_computador} x Jogador {pontos_jogador} ')
    elif opcao == 3:
        pontos_jogador = 0
        pontos_computador = 0
        print('O placar foi resetado!')
    else:
        print('Obrigado por jogar meu jogo!')
        break