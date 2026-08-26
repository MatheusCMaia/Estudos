from datetime import datetime
try:
    idade = int(input('Digite sua idade: '))
    nascimento = datetime.now().year - idade
except Exception as erro:
    print(f'Você digitou algo errado! Erro: {erro}') #Não usar para mostrar para o cliente
else:
    print(f'Você nasceu em: {nascimento}')
finally:
    print('Obrigado por usar meu programa!')