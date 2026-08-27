import json

#convertendo um dicionario em str
alunos = {'nome': 'Matheus', 'idade': '22', 'media': 7, 'situacao': 'Aprovado'}

texto_json = json.dumps(alunos, ensure_ascii=False)

#converter uma str (resposta da API) pra um dicionario
teste_api = '{"nome": "joao", "idade": "19", "media": 2, "situacao": "reprovado"}'
converter = json.loads(teste_api)
print(converter['nome'])
print(type(converter))
