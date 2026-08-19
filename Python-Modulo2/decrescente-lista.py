valores = []
while True:
    numero = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(numero)
    else:
        for i in range(len(valores)):
            if numero > valores[i]:
                valores.insert(i, numero)
                print(valores)
                break
            else:
                valores.insert(i+1,numero)
                print(valores)
                break
    if str(input('Quer continuar? [S/N] ')) in 'Nn':
        break
print(valores)
            

