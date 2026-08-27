import zipfile
import os

pasta_de_destino = "arquivos_dados_empresa"


#verificando a existência da pasta de destino e criando a pasta caso ela não exista
if not os.path.exists(pasta_de_destino):
    os.makedirs(pasta_de_destino)

#extraindo o arquivo comprimido para a pasta de destino
with zipfile.ZipFile('dados_empresa_comprimido.zip', 'r') as zipf:
    zipf.extractall(pasta_de_destino)