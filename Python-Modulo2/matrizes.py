tabela1 = []
tabela2 = []
tabela3 = []
pares = 0
for i in range(9):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares += valor
    if i < 3:
        tabela1.append(valor)
    elif i >= 3 and i < 6:
        tabela2.append(valor)
    else:
        tabela3.append(valor)

tabela4 = []
tabela4.append(tabela1)
tabela4.append(tabela2)
tabela4.append(tabela3)
coluna3 = tabela4[0][2] + tabela4[1][2] + tabela4[2][2]
maior = 0
for i in range(3):
    if tabela4[1][i] > maior:
        maior = tabela4[1][i]
print('-='*13)
print(f'[ {tabela4[0][0]} ] [ {tabela4[0][1]} ] [ {tabela4[0][2]} ]')
print(f'[ {tabela4[1][0]} ] [ {tabela4[1][1]} ] [ {tabela4[1][2]} ]')
print(f'[ {tabela4[2][0]} ] [ {tabela4[2][1]} ] [ {tabela4[2][2]} ]')
print('-='*13)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior}')



