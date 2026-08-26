#reposicionar o cursor
'''with open('exemplo1.txt', 'r+', encoding='UTF-8') as arquivo:
    print(arquivo.read(3))
    arquivo.seek(0)
    print(arquivo.read(5))'''
#ler linhas especificas
'''with open('exemplo2.txt', 'r', encoding='UTF-8') as arquivo:
    for index,linha in enumerate(arquivo):
        if index < 3:
            print(linha.strip())'''
#pratica
with open('exemplo2.txt', 'r+', encoding='UTF-8') as arquivo:
    for index, linha in enumerate(arquivo):
        if index < 3:
            print(linha.strip())
    arquivo.write('Testando\n')
with open('exemplo2.txt', 'r+', encoding='UTF-8') as arquivo:
    print(arquivo.read().strip())