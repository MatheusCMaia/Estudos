import requests

#metodo get para fazer uma solicitação de dados a uma API
requisicao_moedas = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#sempre ver a documentação da API, pois nela diz o formato de como a resposta virá, nesse caso JSON <Response [200]> é TUDO CERTO <404> é ERRO
#print(requisicao_moedas)
#printando em formato json
#print(requisicao_moedas.json())
#criar banco de dados no firebase
#firebase utiliza .json também
requisicao_firebase = requests.get('https://teste-ab7c7-default-rtdb.firebaseio.com/.json')
#print(requisicao_firebase.json())
#metodo post
#precisa passar um DATA para ser colocado no banco de dados
#pegando informações das moedas e colocando em uma variavel
informacoes_moedas = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#colocando as informaçõpes da moeda no firebase
post_firebase = requests.post('https://teste-ab7c7-default-rtdb.firebaseio.com/.json', data=informacoes_moedas)
#alterar algo no banco de dados
dados_1 = '{"Dinheiro": "R$999,9", "Idade": "23", "Nome": "Matheus Augusto"}'
#metodo patch
patch_fire = requests.patch('https://teste-ab7c7-default-rtdb.firebaseio.com/1.json', data=dados_1)
print(patch_fire)
#sempre colocar o .json no final
alterar_informacoes = requests.patch('https://teste-ab7c7-default-rtdb.firebaseio.com/-P0Tsip1827JCkI-Zjz4.json', data=informacoes_moedas)
#metodo delete
delete_fire = requests.delete('https://teste-ab7c7-default-rtdb.firebaseio.com/-P0Tsip1827JCkI-Zjz4.json')
print(delete_fire)