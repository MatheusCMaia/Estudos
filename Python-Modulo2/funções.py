'''

Funções

'''


def calcular_idade_maior_dezoito(idade):
    if idade < 18:
        return print('Ele é menor de idade')
    else:
        return print('Ele é maior de idade')

def calcular_desconto(valor, desconto):
    return valor - (valor* desconto)


#Map usado para transformar a entrada em um determinado tipo no caso int(para receber as entradas e transformar em número para fazer operação)
#.split() usado para receber mais de um valor na entrada para r
valor, desconto = map(int, input().split())
print(calcular_desconto(valor, desconto))



#None na função significa ter espaço para mais uma entrada nela mas ela funciona com ou sem
#Caso não tenha o none a função é obrigada a receber um valor naquele espaço se não dá erro

def calcular_desconto_cupom(valor, desconto, cupom=None):
    if cupom == 'MATHEUS20':
        desconto += 0.2
    return valor - (valor * desconto)

print(calcular_desconto_cupom(100, 0.2))
print(calcular_desconto_cupom(100, 0.2, 'MATHEUS20'))