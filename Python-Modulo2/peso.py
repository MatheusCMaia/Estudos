pessoas = []
while True:
    pessoa = input('Digite o nome da pessoa: ')
    peso = int(input('Digite o peso da pessoa: '))
    lista = []
    lista.append(pessoa)
    lista.append(peso)
    pessoas.append(lista)
    if input('Você quer continuar? [S/N]') in 'Nn':
        break
print(pessoas)

maior_peso = pessoas[0][1]
menor_peso = pessoas[0][1]

for i in range(len(pessoas)):
    if pessoas[i][1] > maior_peso:
        maior_peso = pessoas[i][1]
    elif pessoas[i][1] < menor_peso:
        menor_peso = pessoas[i][1]
print('As pessoas com maior peso são: ')
for i in range(len(pessoas)):
    if pessoas[i][1] == maior_peso:
        print(pessoas[i][0])
print('As pessoas com menor peso são: ')
for i in range(len(pessoas)):
    if pessoas[i][1] == menor_peso:
        print(pessoas[i][0])
