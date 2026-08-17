numero = input('Digite um número: ')
repeticao = numero
numero = ''
for i in repeticao:
    if i == '.':
        print('Encontrei o ponto')
        break
    else:
        numero += i

print(numero)