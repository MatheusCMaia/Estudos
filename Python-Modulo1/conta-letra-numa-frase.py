frase = str(input('Digite uma frase: ')).strip().upper()
primeiro_a = 0
for i in range(len(frase)):
    if frase[i] == 'A':
        primeiro_a += i + 1
        break
ultimo_a = 0
for i in range(len(frase)):
    if frase[i] == 'A':
        ultimo_a = i + 1
quantidade_de_a = 0
for i in frase:
    if i == 'A':
        quantidade_de_a += 1

print(f'A letra A aparece {quantidade_de_a} na frase.')
print(f'A primeira letra A apareceu na posição {primeiro_a}')
print(f'A última letra A apareceu na posição {ultimo_a}')

