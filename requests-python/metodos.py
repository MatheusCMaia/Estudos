import requests

#metodo get para fazer uma solicitação de dados a uma API
requisicao_moedas = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#sempre ver a documentação da API, pois nela diz o formato de como a resposta virá, nesse caso JSON <Response [200]> é TUDO CERTO <404> é ERRO
#print(requisicao_moedas)
#printando em formato json
#print(requisicao_moedas.json())
#criar banco de dados no firebase
#firebase utiliza .json também
requisicao_firebase = requests.get('link do seu firebase (tirei por motivos de segurança)')
#print(requisicao_firebase.json())
#metodo post
#precisa passar um DATA para ser colocado no banco de dados
#pegando informações das moedas e colocando em uma variavel
informacoes_moedas = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#colocando as informaçõpes da moeda no firebase
post_firebase = requests.post('link do seu firebase (tirei por motivos de segurança)', data=informacoes_moedas)
#alterar algo no banco de dados
dados_1 = '{"Dinheiro": "R$999,9", "Idade": "23", "Nome": "Teste"}'
#metodo patch
patch_fire = requests.patch('link do seu firebase (tirei por motivos de segurança)', data=dados_1)
print(patch_fire)
#sempre colocar o .json no final
alterar_informacoes = requests.patch('link do seu firebase (tirei por motivos de segurança)', data=informacoes_moedas)
#metodo delete
delete_fire = requests.delete('link do seu firebase (tirei por motivos de segurança)')
print(delete_fire)