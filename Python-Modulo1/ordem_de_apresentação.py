from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o noem do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
lista_embaralhada = []
contador = 0
while True:
    sortear = choice(lista)
    if contador == 4:
        break
    if sortear not in lista_embaralhada:
        lista_embaralhada.append(sortear)
        contador += 1

for i in range(1,5):
    print(f'O {i}° à apresentar é {lista_embaralhada[i-1]}')


