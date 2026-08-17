algo = input('Digite algo: ')
try:
    algo = int(algo)
except ValueError:
    pass
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabetico? {algo.isalpha()}')
print(f'É alfanumérico {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minusculas? {algo.islower()}')