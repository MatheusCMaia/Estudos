from os import system
system('cls')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'''
O primeiro número: {primeiro_numero}
O segundo número: {segundo_numero}
O número {primeiro_numero} é maior que {segundo_numero}
O primeiro número é maior!''')
elif primeiro_numero < segundo_numero:
    print(f'''
O primeiro número: {primeiro_numero}
O segundo número: {segundo_numero}
O número {primeiro_numero} é menor que {segundo_numero}
O segundo número é maior!''')
else:
    print(f'''
O primeiro número: {primeiro_numero}
O segundo número: {segundo_numero}
O número {primeiro_numero} é igual {segundo_numero}
O dois números são iguais!''')