"""

Crie um programa que:

Pergunte ao usuário:

Nome (string)
Idade (int)
Altura em metros (float)
Peso em kg (float)
Calcule o IMC com a fórmula:

IMC = peso / (altura * altura)
Exiba um resumo do cadastro formatado:

Olá, Maria! 
Você tem 25 anos, mede 1.70m, pesa 65kg e seu IMC é 22.49.
Use operadores relacionais/lógicos para classificar o IMC:

IMC < 18.5 → Abaixo do peso
18.5 ≤ IMC < 25 → Peso normal
25 ≤ IMC < 30 → Sobrepeso
IMC ≥ 30 → Obesidade


"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Olá, ",nome)
    print("Você tem ",nome, "anos, mede", altura,"m, pesa ",peso,"kg e seu IMC é", imc)
    print("Você está abaixo do peso")
if imc < 25 and 18.5 <= imc: 
    print("Olá, ",nome)
    print("Você tem ",nome, "anos, mede", altura,"m, pesa ",peso,"kg e seu IMC é", imc)
    print("Você está com o peso normal")
if imc < 30 and 25 <= imc:
    print("Olá, ",nome)
    print("Você tem ",nome, "anos, mede", altura,"m, pesa ",peso,"kg e seu IMC é", imc)
    print("Você está com sobrepeso")
if imc >= 30:
    print("Olá, ",nome)
    print("Você tem ",nome, "anos, mede", altura,"m, pesa ",peso,"kg e seu IMC é", imc)
    print("Você está obeso")


