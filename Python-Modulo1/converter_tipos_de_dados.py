"""

Conversão de tipos

"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

#Convertendo um INT(idade) em STR(idade) de forma momentanea 
print("Nome: ",nome, "Idade: " + str(idade),  "Altura: ",altura, "Peso: ", peso)

#Exibição da variavel voltando para String
print(idade, type(idade))