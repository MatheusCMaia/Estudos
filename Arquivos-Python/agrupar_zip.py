import zipfile

#comprimir padrão
with zipfile.ZipFile('dados_empresa.zip', 'w') as zipf:
    zipf.write('financeiro.txt')
    zipf.write('funcionarios.txt')

#comprimir mais ainda
with zipfile.ZipFile('dados_empresa_comprimido.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('financeiro.txt')
    zipf.write('funcionarios.txt')

#inspecionar arquivos zip
with zipfile.ZipFile('dados_empresa_comprimido.zip', 'r') as zipf:
    print(f'Arquivos dentros de dados_empresa_comprimido.zip são {zipf.namelist()}')
    #pegar dados de um arquivo especifico
    informacao_arquivo = zipf.getinfo('financeiro.txt')
    print(f'O tamanho original do arquivo financeiro.txt era de: {informacao_arquivo.file_size} bytes')
    print(f'O tamanho do arquivo comprimido foi de {informacao_arquivo.compress_size} bytes')