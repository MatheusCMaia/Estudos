boletim = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, media])
    continuar = str(input('Deseja continuar? '))
    if continuar in 'nN':
        break
print('-='*13)
print('''
No.  Nome     Média
-------------------- 
''')
for i in range(len(boletim)):
    print(f'''
{i+1} {boletim[i][0]}  {boletim[i][1]}
''')