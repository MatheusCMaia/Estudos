import zipfile

#comprimir padrão
with zipfile.ZipFile('dados_empresa.zip', 'w') as zipf:
    zipf.write('financeiro.txt')
    zipf.write('funcionarios.txt')

#comprimir mais ainda
with zipfile.ZipFile('dados_empresa_comprimido.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('financeiro.txt')
    zipf.write('funcionarios.txt')

