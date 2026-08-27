import json 
#ler
with open('livros.json', 'r', encoding='utf-8') as arquivo:
    livros = json.load(arquivo)
    print(livros)
    print(livros[0]['titulo'])

#listar
for livro in livros:
    print(f'{livro['titulo']} - R${livro['preco']:.2f}')

#colocar especificações
print('Livros disponíveis para venda:')
for livro in livros:
    if livro['em_estoque']:
        print(f'{livro['titulo']} - R${livro['preco']:.2f}')

#adicionando dados em .json
novo_livro = {
    "id": 3,
    "titulo": "Duna",
    "autor": "Frank hebert",
    "preco": 65.00,
    "em_estoque": True
  }

livros.append(novo_livro)
print(livros)

with open('livros_atualizados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(livros,arquivo,indent=4,ensure_ascii=False)