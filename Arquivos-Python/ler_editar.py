#abrir e fechar arquivo, precisa lembrar de fechar o arquivo pode causar problema na memória caso de algum erro
'''arquivo = open("teste.txt", 'r', encoding='UTF-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()'''
#abrir e fechar arquivo, sem se preocupar com erros
'''with open('teste.txt', 'r', encoding='UTF-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)'''
#sobrescrever arquivo
'''with open('teste2.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Test 123')'''
#adicionar no final do arquivo
'''with open('teste2.txt', 'a', encoding='UTF-8') as arquivo:
    arquivo.write('\nTest 123')'''
#ler linha por linha
with open('teste2.txt', 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())