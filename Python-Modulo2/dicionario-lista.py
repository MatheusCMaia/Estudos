pessoas = {}
cadastrados = []
soma_idades = 0
while True:
    pessoas['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: '))
        if pessoas['sexo'] not in 'mMfF':
            print('Digite o sexo corretamente!')
        else:
            break
    pessoas['idade'] = int(input('Idade: '))
    while True:
        continuar = str(input('Você quer continuar? [S/N]'))
        if continuar not in 'sSnN':
            print('Digite corretamente!')
            pass
        else:
            break
    cadastrados.append(pessoas)
    soma_idades += pessoas['idade']
    pessoas = {}
    if continuar in 'nN':
        break

print('-='*13)
print(f'Tem {len(cadastrados)} pessoas cadastradas!')
print(f'A média de idade é de {soma_idades/len(cadastrados):.2f}')
print('As mulheres cadastradas foram: ')
for i in cadastrados:
    if i['sexo'] in 'fF':
        print(i['nome'])
print('As pessoas acima da média são: ')
for i in cadastrados:
    if i['idade'] > soma_idades/len(cadastrados):
        print(f'nome = {i['nome']}; sexo = {i['sexo'].upper()}; idade = {i['idade']}')


