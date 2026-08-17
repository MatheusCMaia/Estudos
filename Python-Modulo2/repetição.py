"""

Laço de repetição for

"""

frutas = ['maçã', 'mamão', 'laranja', 'pera', 'banana']

for fruta in frutas:
    print(fruta)

#Começa sempre em 0 
for i in range(5):
    print(i)

#Mostrar o resultado correto
for i in range(5):
    print(i+1)

caixa_de_brinquedos = ['maxsteel', 'pelucia', 'hotweels', 'soldadinho']
brinquedos_para_doacao = []
brinquedos_para_uso = []


#Adicionar item numa outra lista
for brinquedo in caixa_de_brinquedos:
    print(brinquedo)
    if brinquedo in ['pelucia', 'hotweels']:
        print('Opa esse brinquedo eu quero')
        brinquedos_para_uso.append(brinquedo)
    else:
        print('Opa esse brinquedo eu não quero')
        brinquedos_para_doacao.append(brinquedo)

print(brinquedos_para_doacao)
print(brinquedos_para_uso)