largura_parede = float(input('Digite a largura da sua parede: '))
altura_parede = float(input('Digite a altura da sua parede: '))

print(f'A sua parede tem as dimensões {largura_parede}x{altura_parede}e sua área é {largura_parede * altura_parede:.2f}m²')
print(f'Você irá precisar de {(largura_parede * altura_parede) / 2 :.2f} galões de tinta para pintar')