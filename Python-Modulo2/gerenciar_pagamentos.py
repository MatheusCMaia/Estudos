from os import system
system('cls')

print('''
==============
LOJA DO SEU ZÉ
==============

Qual será sua forma de pagamento?

[1] À VISTA NO DINHEIRO/CHEQUE (10% DE DESCONTO)
[2] À VISTA NO CARTÃO (5% DE DESCONTO)
[3] 2x NO CARTÃO (PREÇO NORMAL)
[4] 3x NO CARTÃO OU MAIS (20% DE JUROS)


''')
valor_da_compra = float(input('Digite o valor da compra: '))
opcao_pagamento = int(input('Digite sua forma de pagamento: '))

if opcao_pagamento == 1: 
    print(f'Você irá pagar {valor_da_compra - (valor_da_compra * 0.1)}')
    print('Obrigado por comprar na loja do seu zé')
elif opcao_pagamento == 2:
    print(f'Você irá pagar {valor_da_compra - (valor_da_compra * 0.05)}')
    print('Obrigado por comprar na loja do seu zé')
elif opcao_pagamento == 3:
    print(f'Você irá pagar {valor_da_compra}')
    print('Você irá pagar em duas parcelas!')
    print(f'O valor de cada parcela será {valor_da_compra/2}')
else:
    while True:
        parcelas = int(input('Em quantas parcelas você deseja parcelar? '))
        if parcelas < 3:
            print('Você selecionou a opção de parcerlar 3x ou mais!')
            print('Digite a parcela corretamente!')
        else:
            print(f'Você vai parcelar em {parcelas}')
            print(f'O valor total da compra com 20% de juros será: {valor_da_compra + (valor_da_compra * 0.2)}')
            print(f'O valor da parcela será R${(valor_da_compra + (valor_da_compra * 0.2)) / parcelas}')
            break