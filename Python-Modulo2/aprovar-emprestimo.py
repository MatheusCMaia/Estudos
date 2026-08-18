valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o seu salário: '))
quantidade_parcelas = int(input('Em quantos anos você quer pagar? ')) * 12

if valor_casa / quantidade_parcelas < valor_salario * 0.3:
    print('Seu emprestimo foi aceito!')
    print(f'O valor da parcela é {valor_casa/quantidade_parcelas:.2f}!')
else:
    print('Seu emprestimo foi negado!')