nome_completo = str(input('Digite seu nome completo: ')).split()
condicao = 0
for i in nome_completo:
    if i.upper() == 'SILVA':
        condicao += 1
print('Seu nome tem Silva' if condicao >= 1 else 'Seu nome não tem silva')
