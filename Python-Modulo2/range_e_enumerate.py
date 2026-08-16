"""

3 S = Start, Stop e Step
range()

"""

#Colocando um start no range
for i in range(1, 10):
    print(i)

print('-'*10)

#Colocando um step no range
for i in range(1, 10, 5):
    print(i)

usuarios = ['Matheus', 'Andre', 'Julia', 'Marcos', 'Rodrigo', 'Marcela']

for indice, user in enumerate(usuarios, 1):
    print(f'Indice: {indice} - {user}')