from random import randint
with open('financeiro.txt', 'w', encoding='utf-8') as financias:
    for i in range(30):
        lucro = str(randint(0,100))
        financias.write(f'{lucro}\n')

with open('funcionarios.txt', 'w', encoding='utf-8') as colaboradores:
    funcionarios = ['Matheus', 'Fernanda', 'Humberto', 'Aurea']
    for i in funcionarios:
        colaboradores.write(f'{i}\n')
