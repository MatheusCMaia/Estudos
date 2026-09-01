from pathlib import Path
from shutil import rmtree

#caminho até a pasta
caminho_projeto = Path()
print(caminho_projeto.absolute())


#caminho completo até o arquivo
caminho_arquivo = Path(__file__)
print(caminho_arquivo)


#caminho da pasta mãe
print(caminho_arquivo.parent)


#caminho da pasta mãe da pasta mãe podendo até chegar na pasta mãe
print(caminho_arquivo.parent.parent)

#criar novos caminhos
pasta_nova = caminho_arquivo.parent / 'pasta_nova'
print(pasta_nova)
print(pasta_nova / 'teste')


#pegar o caminho da pasta home
print(Path.home())

#criar arquivo no caminho que eu quero
caminho_arquivo = Path.home() / 'Desktop' / 'criandoarquivospathlib.txt'
caminho_arquivo.touch()

#escrevendo em um arquivo
caminho_arquivo.write_text('Testando')

#escrevendo em um arquivo de outra maneira com with
with caminho_arquivo.open('a+') as file:
    file.write('\nLinha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

#ler um arquivo com pathlib
print(caminho_arquivo.read_text())

#deletando um arquivo com o caminho
caminho_arquivo.unlink()

#criando um diretorio
criando_diretorio = Path.home() / 'Desktop' / 'criando_diretorio'
criando_diretorio.mkdir(exist_ok=True)

#criar um diretorio dentro de um diretorio
criando_diretorio_diretorio = criando_diretorio / 'diretorio dentro de diretorio'
criando_diretorio_diretorio.mkdir(exist_ok=True)

#criar arquivo dentro de um diretorio dentro do outro
mais_um_arquivo = criando_diretorio_diretorio / 'mais_um_arquivo.py'
mais_um_arquivo.touch()


#deletando um diretorio
#criando_diretorio.rmdir()

#deletando um diretorio não vazio
rmtree(criando_diretorio)







