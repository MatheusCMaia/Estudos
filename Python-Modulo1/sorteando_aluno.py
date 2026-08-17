import random
alunos = []

while True:
    entrada = int(input('''

Digite 1 - Para adicionar mais um aluno
Digite 2 - Para sortear
Digite 3 - Para mostrar os alunos adicionados
Digite 4 - Para encerrar

'''))
    if entrada == 4:
        break
    elif entrada == 1:
        alunos.append(input('Digite o nome do aluno que você quer adicionar'))
        print('O aluno foi adicionado com sucesso!')
    elif entrada == 2 and len(alunos) == 0:
        print('Nenhum aluno foi adicionado, até o momento.')
    elif entrada == 2:
        sorteio = random.choice(alunos)
        print(f'O aluno {sorteio} foi sorteado!')
    elif entrada == 3:
        print('Os alunos listados até o momento foram')
        for i in alunos:
            print(f'--- {i}')
