while True:
    numero = input('Digite um número que você deseja ver a tabuada: ')
    try:
        numero = int(numero)
        break
    except ValueError:
        print('Por favor digite um número')

print('-' * 10)
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')
print('-' * 10)