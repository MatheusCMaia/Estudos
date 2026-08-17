while True:
    numero = input('Digite um número: ')
    try:
        numero = int(numero)
        break
    except ValueError:
        print('Por favor digite um número')

print(f'O número é {numero}, seu antecessor é {numero - 1} e seu sucessor é {numero + 1}')