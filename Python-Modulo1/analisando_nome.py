nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
primeiro_nome = ''
for i in nome:
    if i == ' ':
        break
    elif i != ' ':
        primeiro_nome += i
nome = nome.upper()
print(f'Seu nome em maiusculo é: {nome}')
nome = nome.lower()
print(f'Seu nome em minusculas é: {nome}')
contador = 0
for i in nome:
    if i == ' ':
        pass
    else:
        contador += 1
print(f'O número de letras do seu nome é: {contador}')
print(f'Seu primeiro nome é {primeiro_nome}')
