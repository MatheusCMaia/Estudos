"""

Utilização do while

"""

idade = 0

#Executa infinito pois o requisito para sair nunca será alcançado
#while idade <= 18:
    #print(idade)


#Colocada uma trava para sair do laço infinito de repetição
#Boa prática colocar sempre uma variavel de controle dentro do laço de repetição while
while idade <= 18:
    print(idade)
    idade += 1 

print('sai desse fluxo')


senha_user = "123456"

while True:
    senha_entrada = input('Digita sua senha: ')
    if senha_entrada == senha_user:
        print('Login feito com sucesso!')
        break
    else:
        print('Senha errada, tente novamente!')



