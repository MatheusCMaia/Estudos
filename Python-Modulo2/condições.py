"""

Condicionais if, elif e else

"""


idade = 18

if idade > 18:
    print("Você é maior de 18 anos")
elif idade == 18:
    print("Você tem exatamente 18 anos")
else:
    print("Você não é maior de idade")


#Casos comuns e que devem ser evitados

if idade > 18:
    print("Você é maior de 18 anos")
if idade == 18:
    print("Você tem exatamente 18 anos")
if idade > 18 and idade < 25:
    print("VSua idade está entre 18 e 25 anos")

