class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao =descricao
        self.inscritos = inscritos
    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

canal_matheus = Canal('Matheuszinho', 'Descrição do meu canal é', 10000)
canal_guanabara = Canal('Curso em vídeo', 'Paixão por ensinar', 250000)
print(f'Quantidade de inscritos atuais: {canal_matheus.inscritos}')
canal_matheus.inscrever()
print(f'Quantidade de inscritos atuais {canal_matheus.inscritos}')
