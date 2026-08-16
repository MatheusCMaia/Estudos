nomes = []
idades = []
criancas = 0
adolescentes = 0
adultos = 0
idosos = 0
def cadastrar_usuario(nome,idade):
    nomes.append(nome)
    idades.append(idade)
    return

while True:
    print('''
     1 - Cadastrar usuário
     2 - Listar usuários
     3 - Analisar idades
     4 - Sair
''')
    entrada = int(input('Escolha: '))
    if entrada == 1:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar_usuario(nome, idade)
        print('Usuário cadastrado com sucesso!')
    elif entrada == 2 and len(nomes) != 0:
        for i in range(len(nomes)):
            print(f'{i+1} - {nomes[i]} {idades[i]} anos')
    elif entrada == 2 and len(nomes) == 0:
        print('Não tem nomes cadastrados')
    elif entrada == 3 and len(idades) == 0:
        print('Não tem idades cadastradas')
    elif entrada == 3 and len(idades) != 0:
        for i in range(len(idades)):
            if idades[i] < 12:
                criancas += 1
            elif idades[i] >= 12 and idades[i] < 18:
                adolescentes += 1
            elif idades[i] >= 18 and idades[i] < 60:
                adultos += 1
            else:
                idosos += 1
        print(f'''
        Crianças: {criancas}
        Adolescentes: {adolescentes}
        Adultos: {adultos}
        Idosos: {idosos}

''')
    else:
        print('Encerrando o sistema')
        break