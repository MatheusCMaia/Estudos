while True:
    numero = input('Digite um número: ')
    try:
        numero = int(numero)
        break
    except ValueError:
        print('Por favor digite um número')

print(f'O dobro de {numero} é {numero * 2}')
print(f'O triplo de {numero} é {numero * 3}')
print(f'A raiz é {numero} é {numero ** (1/2):.2f}')

